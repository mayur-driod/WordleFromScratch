from fastapi import FastAPI

app = FastAPI()

def healthroute():
    return {"Status" : "Wokay"}

@app.get("/")
async def root():
    return {"Message":["Hello World!","HW",1,2,3,4,5]}

@app.get("/health")
async def root():
    return healthroute()