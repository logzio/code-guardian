#!/usr/bin/env bash
echo "Copying necessary files..."
mkdir ~/.docker-guard
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/docker-guardian/guardian-script.py > ~/.docker-guard/guardian-script.py
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/docker-guardian/docker-func >> ~/.zshrc
echo "Everything is ready, you can now write dockers safely!"
