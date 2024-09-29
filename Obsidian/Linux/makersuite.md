### API keys

MakerSuite creates a new Google Cloud project for each new API key. You also can create an API key in an existing Google Cloud project. All projects are subject to the [Google Cloud Platform Terms of Service open_in_new](https://cloud.google.com/terms).

Note: The PaLM API is currently in public preview. Production applications are not supported yet.

API key
`AIzaSyAhjff6i4So6aJLd94OEDbGdI34m1LfoeM

```bash
curl \ -H 'Content-Type: application/json' \ -d '{ "prompt": { "hello,ai": "Write a story about a magic backpack"} }' \ "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=AIzaSyAhjff6i4So6aJLd94OEDbGdI34m1LfoeM"
```