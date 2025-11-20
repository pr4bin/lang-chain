import uvicorn
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from frontend import App

app = FastAPI()
configure(app, App)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)