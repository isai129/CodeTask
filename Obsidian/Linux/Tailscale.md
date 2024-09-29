Manually install onAmazon Linux 2Arch LinuxCentOS 7CentOS 8CentOS Stream 9Debian BookwormDebian BullseyeDebian BusterDebian SidDebian StretchFedoraNixOSopenSUSE Leap 15.1openSUSE Leap 15.2openSUSE TumbleweedOracle Linux 7Oracle Linux 8RHEL 8RHEL 9Raspberry Pi BullseyeRaspberry Pi BusterRaspberry Pi StretchUbuntu 16.04 LTS (Xenial)Ubuntu 18.04 LTS (Bionic)Ubuntu 19.10 (Eoan)Ubuntu 20.04 LTS (Focal)Ubuntu 20.10 (Groovy)Ubuntu 21.04 (Hirsute)Ubuntu 21.10 (Impish)Ubuntu 22.04 LTS (Jammy)Other

Packages are available for x86 and ARM CPUs, in both 32-bit and 64-bit variants.

1. Add Tailscale’s package signing key and repository:
    
    ```
    curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/jammy.noarmor.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
    curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/jammy.tailscale-keyring.list | sudo tee /etc/apt/sources.list.d/tailscale.list
    ```
    
2. Install Tailscale:
    
    ```
    sudo apt-get update
    sudo apt-get install tailscale
    ```
    
3. Connect your machine to your Tailscale network and authenticate in your browser:
    
    ```
    sudo tailscale up
    ```
    
4. You’re connected! You can find your Tailscale IPv4 address by running:
    
    ```
    tailscale ip -4
    ```
    

If the device you added is a server or remotely-accessed device, you may want to consider [disabling key expiry](https://tailscale.com/kb/1028/key-expiry) to prevent the need to periodically re-authenticate.


## Subnet routers and traffic relay nodes

Tailscale works best when the client app is installed directly on every client, server, and VM in your organization. That way, traffic is end-to-end encrypted, and no configuration is needed to move machines between physical locations.

However, in some situations, you can’t or don’t want to install Tailscale on each device:

- With embedded devices, like printers, which don’t run external software
- When connecting large quantities of devices, [like an entire AWS VPC](https://tailscale.com/kb/1021/install-aws)
- When incrementally deploying Tailscale (eg. on legacy networks)

In these cases, you can set up a “subnet router” (previously called a relay node or relaynode) to access these devices from Tailscale. **Subnet routers act as a gateway**, relaying traffic from your Tailscale network onto your physical subnet. Subnet routers respect features like [access control policies](https://tailscale.com/kb/1018/acls), which make it easy to migrate a large network to Tailscale without installing the app on every device.

![A diagram showing how subnet routers relay traffic between a subnet (eg. your local network) and Tailscale, connecting devices that can't install Tailscale.](https://tailscale.com/kb/1019/subnets/subnets.png)

Devices behind a subnet router _do not_ count toward your [pricing plan’s device limit](https://tailscale.com/pricing). However, we encourage you to install Tailscale directly on devices wherever possible, for better performance, security, and a zero-configuration setup.

Subnet routers are available for [**all plans**](https://tailscale.com/pricing/).

### [Setting up a subnet router](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#setting-up-a-subnet-router) 

To activate a subnet router on a fresh Linux, macOS, or Windows machine, follow these steps:

#### [Step 1: Install the Tailscale client](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#step-1-install-the-tailscale-client) 

LinuxmacOSWindows

[Download and install Tailscale](https://tailscale.com/download/linux) onto your subnet router machine. We offer instructions for a variety of Linux distros.

#### [Step 2: Connect to Tailscale as a subnet router](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#step-2-connect-to-tailscale-as-a-subnet-router) 

Once installed, you can start (or restart) Tailscale as a subnet router:

LinuxmacOSWindows

This feature requires IP forwarding to be enabled.

##### [Enable IP forwarding](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#enable-ip-forwarding) 

If your Linux system has a `/etc/sysctl.d` directory, use:

```shell
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf
```

Otherwise, use:

```shell
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p /etc/sysctl.conf
```

If your Linux node uses `firewalld`, you may need to also allow masquerading due to a [known issue](https://github.com/tailscale/tailscale/issues/3416). As a workaround, you can allow masquerading with this command:

```shell
firewall-cmd --permanent --add-masquerade
```

Other distros may require different steps.

When enabling IP forwarding, ensure your firewall is set up to deny traffic forwarding by default. This is a default setting for common firewalls like `ufw` and `firewalld`, and ensures your device doesn’t route traffic you don’t intend.

##### [Advertise subnet routes](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#advertise-subnet-routes) 

```
sudo tailscale up --advertise-routes=192.168.0.0/24,192.168.1.0/24
```

Replace the subnets in the example above with the right ones for your network. Both IPv4 and IPv6 subnets are supported.

If the device is authenticated by a user who can advertise the specified route in [`autoApprovers`](https://tailscale.com/kb/1018/acls/#auto-approvers-for-routes-and-exit-nodes), then the subnet router’s routes will automatically be approved. You can also advertise any subset of the routes allowed by `autoApprovers` in the tailnet policy file.

If you’d like to expose default routes (0.0.0.0/0 and ::/0), consider using [exit nodes](https://tailscale.com/kb/1103/exit-nodes) instead.

#### [Step 3: Enable subnet routes from the admin console](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#step-3-enable-subnet-routes-from-the-admin-console) 

This step is not required if using `autoApprovers`.

Open the [**Machines**](https://login.tailscale.com/admin/machines) page of the admin console, and locate the device that advertised subnet routes. You can look for the **Subnets** badge in the machines list, or use the [`property:subnet` filter](https://login.tailscale.com/admin/machines?q=property%3Asubnet) to see all devices advertising subnet routes. Using the ![ellipsis icon](https://tailscale.com/files/images/icons/fa-ellipsis-h.svg) menu at the end of the table, select **Edit route settings**. This will open up the **Edit route settings** panel.

Click **Approve all** on your routes so that Tailscale distributes the subnet routes to the rest of the nodes on your Tailscale network. Alternatively, you can approve each route individually by clicking the toggle to the left of the route.

![The subnet settings modal](https://tailscale.com/kb/1019/subnets/subnets-modal.png)

You may prefer to disable key expiry on your server to avoid having to periodically reauthenticate. See [key expiry](https://tailscale.com/kb/1028/key-expiry) for more information about machine keys and how to disable their expiry. If you are using [ACL tags](https://tailscale.com/kb/1068/acl-tags/), [key expiry is disabled by default](https://tailscale.com/kb/1068/acl-tags/#key-expiry-for-tagged-devices).

#### [Step 4: Add ACL rules for the advertised subnet routes](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#step-4-add-acl-rules-for-the-advertised-subnet-routes) 

This step is not required if you already have rules that allow access to your advertised subnet routes.

Open the [**Access Controls**](https://login.tailscale.com/admin/acls) page of the admin console to update your [tailnet policy file](https://tailscale.com/kb/1018/acls), and create an ACL rule that allows access to the advertised subnet.

**What this ACL does:**

- Members of the development team `group:dev` can access devices in the subnets `192.168.0.0/24` and `192.168.1.0/24`.
- The subnet `192.168.0.0/24` can access the subnet `192.168.1.0/24` and vice versa, if [subnet route masquerading](https://tailscale.com/kb/1023/troubleshooting/#how-can-i-disable-subnet-route-masquerading) is disabled.

```json
{
  "groups": {
    "group:dev": ["alice@example.com", "bob@example.com"]
  },
  "acls": [
    // Users in group:dev and devices in subnets 192.168.0.0/24 and
    // 192.168.1.0/24 can access devices in subnets 192.168.0.0/24 and
    // 192.168.1.0/24
    { "action": "accept",
      "src": ["group:dev","192.168.0.0/24", "192.168.1.0/24"],
      "dst": ["192.168.0.0/24:*", "192.168.1.0/24:*"]
    }
  ]
}
```

Click **Save** on your tailnet policy file so the Tailscale coordination server distributes the updated policy to the nodes in your tailnet.

#### [Step 5: Verify your connection](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#step-5-verify-your-connection) 

Check that you can ping your new subnet routers’s Tailscale IP address from your personal Tailscale machine (Windows, macOS, etc). You can find the Tailscale IP in the [**admin console**](https://login.tailscale.com/admin), or by running this command on the subnet router.

```
tailscale ip -4
```

#### [Step 6: Use your subnet routes from other machines](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#step-6-use-your-subnet-routes-from-other-machines) 

Clients on Windows, macOS, iOS, and Android will automatically pick up your new subnet routes.

For Linux clients, only those using `--accept-routes` flag will discover the new routes, since the default is to use only the [Tailscale 100.x addresses](https://tailscale.com/kb/1015/100.x-addresses). Enable this by running:

```
sudo tailscale up --accept-routes
```

#### [Updating subnet routes](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#updating-subnet-routes) 

To later update subnet routes, follow steps 2 to 5 with the new routes.

During step 3 from the [**admin console**](https://login.tailscale.com/admin), previously enabled routes that you no longer included in step 2 will no longer appear as advertised, noted by the icon to the right of the route. You can choose to remove the routes completely, or keep them enabled if you plan to re-advertise them in the future.

![The subnet settings modal](https://tailscale.com/kb/1019/subnets/not-advertised-subnets.png)

#### [Optional: Route DNS lookups to an internal DNS server](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#optional-route-dns-lookups-to-an-internal-dns-server) 

You may add [Tailscale IPs to public DNS records](https://tailscale.com/kb/1054/dns), since Tailscale IPs are only accessible to authenticated users of your network. However, if you’d prefer to use an internal DNS server on your subnet, you can do so by configuring split DNS in the [**DNS**](https://login.tailscale.com/admin/dns) page of the admin console.

#### [Optional: Set up high availability](https://tailscale.com/kb/1019/subnets?slug=kb&slug=1019&slug=subnets#optional-set-up-high-availability) 

You can set up high availability to ensure your network is connectable even if one subnet router goes offline. For more information, see our article on [high availability failover](https://tailscale.com/kb/1115/high-availability).

Last updated Dec 12, 2023