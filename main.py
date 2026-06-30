from fastapi import FastAPI

app = FastAPI()

# Store data
data = []

# GET Method
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# POST Method (Insert)
@app.post("/add")
def add_item(item: str):
    data.append(item)
    return {
        "message": "Item Added Successfully",
        "data": data
    }

# PUT Method (Update)
@app.put("/update")
def update_item(index: int, item: str):
    if index < len(data):
        data[index] = item
        return {
            "message": "Item Updated Successfully",
            "data": data
        }
    return {"message": "Invalid Index"}

# DELETE Method (Delete)
@app.delete("/delete")
def delete_item(index: int):
    if index < len(data):
        data.pop(index)
        return {
            "message": "Item Deleted Successfully",
            "data": data
        }
    return {"message": "Invalid Index"}