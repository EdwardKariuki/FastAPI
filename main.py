import os
from fastapi import Body, FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import openai
from pydantic import BaseModel, ValidationError


API_KEY: str = os.getenv('API_KEY')

app = FastAPI()


class Post(BaseModel):
    prompt: str
 
 
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/openai")
def open_ai(new_post: Post = Body(..., embed=True)):

    openai.api_key = API_KEY
    model = 'text-davinci-002'
    response = openai.Completion.create(engine=model, prompt=new_post.prompt, 
                                        max_tokens=1024, n=1)
    projections = response.choices[0].text
    
    if new_post.prompt is None:
        raise HTTPException(status_code=400, detail="Please enter a value")
    return {"response": projections}


@app.post("/items/")
def create_item(new_item: Item):
    if new_item.price <= 0:
        raise HTTPException(status_code=400, 
                            detail="Price must be greater than zero")
    return {"item": new_item}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "loc": error["loc"],
            "msg": "Custom error message for {}".format(error["msg"]),
            "type": error["type"]
        })
    return JSONResponse(
         status_code=422, 
         content={"detail": errors})
        