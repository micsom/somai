from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"SomAi": "Smart Home Backend Active"}
