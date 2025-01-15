from fastapi import FastAPI
import uvicorn
from api import router

app = FastAPI()

app.include_router(router)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.101.43.41", port=8000, workers=8,
                reload=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
