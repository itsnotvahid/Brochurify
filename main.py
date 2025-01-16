from fastapi import FastAPI
import uvicorn
from api import router
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    host = os.getenv("HOST", "127.101.43.41")
    port = int(os.getenv("PORT", 8329))
    uvicorn.run("main:app", host="127.101.43.41", port=port,
                reload=True)
