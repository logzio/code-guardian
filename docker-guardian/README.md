# Docker Build Guardian
The Docker Build Guardian is a plugin which performs automated checks on your files in every docker you build to prevent hard-coded sensitive data (such as Shipping Tokens, API Tokens, etc.) from being inserted to a docker image.

To enable the Docker Build Guardian, Run these commands:

```
curl -sSL https://raw.githubusercontent.com/logzio/code-guardian/master/docker-guardian/quickstart.sh | bash -s
source ~/.zshrc
```

### That's it!

## Adding Customized Tests
#### To add your own tests for a specific sensitive expression:
#### Build a function
Build your function as follows:
* Input: String.
* Output: Boolean that indicates whether the string contains the sensitive expression.
 
#### Add the function
 * Add your function to the "function_map" structure in the 'guardian-script.py' as follows:\
    <"Type of expression">: <function_name>
