When you use pip to install Python packages, you may encounter an ‘externally-managed-environment’ error.  

```bash
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.

    If you wish to install a Python library that isn't in Homebrew,
    use a virtual environment:

    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install xyz

    If you wish to install a Python application that isn't in Homebrew,
    it may be easiest to use 'pipx install xyz', which will manage a
    virtual environment for you. You can install pipx with

    brew install pipx
    ...
```

### [](https://dev.to/luca1iu/how-to-fix-the-externally-managed-environment-error-when-using-pip-2omo#solution-1-use-a-virtual-environment)Solution 1: use a virtual environment

create a virtual environment folder in your root path  

```bash
python3 -m venv ~/py_envs
source ~/py_envs/bin/activate
python3 -m pip install xyz
```

### [](https://dev.to/luca1iu/how-to-fix-the-externally-managed-environment-error-when-using-pip-2omo#solution-2-force-install)Solution 2: force install

add `--break-system-packages` at the end of `pip` , for example:  

``` bash
pip install xyz --break-system-packages 
```