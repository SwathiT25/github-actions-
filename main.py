from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello  "}

@app.get("/status")
def get_status():
    return {"status": "FastAPI is running fine 🚀"}


# test -05





