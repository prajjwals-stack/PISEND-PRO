"""
Main
"""
from fastapi import FastAPI


app=FastAPI()

@app.get('/')
def home():
    return "hello world"


@app.post('/SignIn')
def login(username, password):
    return {'username': username, 'password': password}

@app.post('/SignUp')
def SignUp(username, email, password, confirm_password):
    return {'username': username, 'email': email, 'password': password  }
