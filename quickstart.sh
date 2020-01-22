#!/usr/bin/env bash
echo "Copying necessary files..."
sudo easy_install pip
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/pre-commit >> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/guardian-script.py > .git/hooks/guardian-script.py
pip install pathlib
echo "Everything is ready, you can now code safely!"
