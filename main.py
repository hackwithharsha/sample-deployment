from fastapi import FastAPI, FastAPI

app = FastAPI()

@app.get('/user/greeting')
def say_hello():
    return {'greeting': 'Hello world'}
