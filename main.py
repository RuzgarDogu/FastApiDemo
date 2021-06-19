from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    r = {
        'data': {
            'foo':'bar',
            'bar': 3
        }
    }
    return r

@app.get('/about')
def about():
    r = {
        'data': {
            'about':'bar',
            'bar': 3
        }
    }
    return r
