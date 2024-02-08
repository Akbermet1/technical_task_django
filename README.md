## Running the application
1) rename the .env_example file to .env
2) generate a secret key and save the value in the .env file
3) create a virtual environment: python3 -m venv venv
4) activate the virtual environment: source venv/bin/activate
5) install the dependencies: pip install -r requirements.txt 
6) apply the migrations: python manage.py migrate
7) run the server: python manage.py runserver


## To generate a token and test authenticated operations of views
http://localhost/user/api-token-auth/ 
when valid username and password fields are POSTed using form data or JSON, you will receive a Token 

## Testing endpoints in Postman
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
