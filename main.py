from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {" hiii"}

@app.get("/status")
def get_status():
    return {"status": "FastAPI is running fine!!!!!! 🚀"}


# test -11

# test-4





