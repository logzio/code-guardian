# Git Pre-commit Guardian
The Git Pre-commit Guardian is a tool which performs automated checks on your staged-to-be-commited files in your git repository to prevent hard-coded sensitive data (such as Shipping Tokens, API Tokens, etc.) from being commited.

To enable the pre-commit guardian, first cd to your repository you want to protect:

```
cd ~/logzio/your/repo
```

Then run:

```
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/git-guardian/quickstart.sh | bash -s
```
When the Guardian finds possible sensitive data and you wish to commit your changes anyway use this command:
```
git commit -n
```
That's it!
