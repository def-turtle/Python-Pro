from typing import Optional

from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI(title="FastAPI")



# -----------------------
# default
# -----------------------
@app.get("/", tags=["default"])
async def root():
    return {"message": "Root"}

@app.get("/hello/{name}", tags=["default"])
async def hello(name: str):
    return {"Hello": name}


# -----------------------
# example-simple (mounted sub-app)
# -----------------------
example_app = FastAPI(
    title="example-simple",
    openapi_url=None,   # hide separate OpenAPI for the sub-app
    docs_url=None,      # hide separate docs for the sub-app
    redoc_url=None,     # hide separate redoc for the sub-app
)


class APIrouter:
    pass


example_simple_router = APIrouter(prefix="/simple", tags=["example-simple"])
@example_app.get("/hi", tags=["example-simple"], response_class=PlainTextResponse)
async def example_hi(name: str = "World", age: int = 50) -> str:
    return f"Hi, {name} ({age})"

@example_app.get("/hi/{name}", tags=["example-simple"], response_class=PlainTextResponse)
async def example_hi_name(name: str, age: int = 50) -> str:
    return f"Hi, {name} ({age})"

@example_app.get("/hi/{name}/{age}", tags=["example-simple"], response_class=PlainTextResponse)
async def example_hi_name_age(name: str, age: int) -> str:
    return f"Hi, {name} ({age})"

@example_app.get("/hello", tags=["example-simple"])
async def example_hello(
    name: str = Query(default="World"),
    age: int = Query(default=50),
):
    return {"Hello": name, "age": age}

example_app.include_router(example_simple_router)
app.mount("/example-simple", example_app)