from fastapi import FastAPI
from routes import router
import uvicorn



app = FastAPI()

@app.get("healthy")
def healthy():
    return {"status":"ok"}


app.include_router(
        router
)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



