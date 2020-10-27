from flask import Flask, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from flask import url_for, render_template
import os
app = Flask(__name__)
oauth = OAuth(app)


app.secret_key ='random secret'

#oauth config
google = oauth.register(
    name='google',
    client_id='639306762378-fd4sai5fdmt5e21r1o3b01qo7vjajmgg.apps.googleusercontent.com',
    client_secret='_UVWAQD9zn0zKKcq8wRCdcxB',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)


@app.route('/')
def hello_world():
    email = dict(session).get("email", None)
    return f'Hello, {email}!'

@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    #google = oauth.create_client('google')
    #token = oauth.google.authorize_access_token()
    #resp = oauth.google.get("user_info")
    #user_info = resp.json()
    # do something with the token and profile
    return redirect('/')


if __name__ == "__main__":
    app.run(ssl_context='adhoc')