## Project setup (non-obvious steps)
1) rename the .env_example file to .env
2) generate a secret key and save the value in the .env file

## To generate a token and test authenticated operations of views
http://localhost/user/api-token-auth/ 
when valid username and password fields are POSTed using form data or JSON, you will receive a Token 

## Testing endpoints in Postman
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
