from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
post_req_num = 0
get_req_num = 0
launch_code_num = 0
with open("get-post-app.txt", "r") as f:
    launch_code_num = f.read()
with open("get-post-app.txt", "w") as f:
    f.write(str(int(launch_code_num)+1))
    print(launch_code_num)
launch_code_num = int(launch_code_num)+1

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    global launch_code_num
    global get_req_num
    get_req_num += 1
    with open("get_rq.txt", "a") as f:
        f.write(f"Code launch number: {str(int(launch_code_num))} \n")
        f.write(f"Get request number: {get_req_num}"+"\n")
        f.write(f"Item ID: {item_id}"+"\n")
        f.write(f"Query: {q}"+"\n")
        f.write("\n")
    return {"item_id": item_id, "q": q}
@app.post("/items/")
def create_item(item: Item):
    with open("post_rq.txt", "a") as f:
        global launch_code_num
        global post_req_num
        post_req_num += 1
        f.write(f"Code launch number: {str(int(launch_code_num))} \n")
        f.write(f"Post request number: {post_req_num}"+"\n")
        f.write(f"Name: {item.name}"+"\n")
        f.write(f"Price: {item.price}"+"\n")
        f.write(f"Is offer: {item.is_offer}"+"\n")
        f.write("\n")
    return item
