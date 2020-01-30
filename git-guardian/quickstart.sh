#!/usr/bin/env bash
echo "Copying necessary files..."
sudo easy_install pip
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/git-guardian/pre-commit >> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/git-guardian/guardian-script.py > .git/hooks/guardian-script.py
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/utils.py > .git/hooks/utils.py
pip install pathlib
echo "Everything is ready, you can now code safely!"
