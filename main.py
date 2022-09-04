from fastapi import FastAPI

app = FastAPI()


@app.get("/test1")
async def test_one():
    return "this is test1"


@app.get("/test2")
async def test_two():
    return "this is test2"


@app.get("/test3")
async def test_three():
    return "this is test3"
    