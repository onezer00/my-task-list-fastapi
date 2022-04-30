from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"AppName": "FAST LIST WITH PYTHON"}


@app.get("/version")
async def read_item():
    return {"AppVersion": app.version}

if __name__ == "__main__":
    uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)