from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Online Cinema FLEX is alive!"}
