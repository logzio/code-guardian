#!/usr/bin/env bash
echo "Copying necessary files..."
mkdir ~/.docker-guard
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/guardian-script.py > ~/.docker-guard/guardian-script.py
echo "Everything is ready, you can now code safely!"
