from fastapi import FastAPI
import uvicorn

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
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)