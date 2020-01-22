echo "Copying neccesary files..."
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/pre-commit >> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/guardian-script.py >> .git/hooks/guardian-script.py
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/regex.py >> .git/hooks/regex.py

echo "Everything is ready, you can now code safely!"