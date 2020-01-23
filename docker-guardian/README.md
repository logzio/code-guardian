# Docker Build Guardian
The Docker Build Guardian is a plugin which performs automated checks on your files in every docker you build to prevent hard-coded sensitive data (such as Shipping Tokens, API Tokens, etc.) from being inserted to a docker image.

To enable the Docker Build Guardian, Run these commands:

```
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/docker-guardian/quickstart.sh | bash -s
source ~/.zshrc
```

That's it!

