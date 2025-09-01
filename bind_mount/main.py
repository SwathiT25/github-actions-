from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {" hello"}

@app.get("/status")
def get_status():
    return {"status": "FastAPI is running fine!!!!!! 🚀"}


# test -11

# test-4





