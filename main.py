from typing import Union


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}




