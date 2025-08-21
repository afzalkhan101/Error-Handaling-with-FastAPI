from fastapi import FastAPI , HTTPException  

app = FastAPI() 
items = [] 
@app.get("/items/{item_id}")

def get_item(item_id:str):
    
    if item_id not in items:
        raise HTTPException(status_code=404 , detail= "item not found")
    return items[item_id]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if not user_exists(user_id):
        raise HTTPException(
            status_code=404,
            detail="User not found",
            headers={"X-Error-Code": "USER_NOT_FOUND"}
        )