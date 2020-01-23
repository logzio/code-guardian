#!/usr/bin/env bash
mkdir ~/.docker-guard
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/guardian-script.py > ~/.docker-guard/guardian-script.py
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/docker-func >> ~/.zshrc
pip install pathlib
