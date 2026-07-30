from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rootPath():
    return {"message": "Hello!, Welcome to FastAPI contact project"}


@app.get("/contact")  
def get_contacts():
    return {"message": "Contacts List..."}

@app.post("/contact")
def create_contact():
    return {"message": "contact created successfully!"}

@app.patch("/contact/{id}")
def update_contact(id: int):
    return {"message": f"Updated for id: {id}"}

@app.delete("/contact/{id}")
def delete_contact(id: int):
    return {"message": f"deleted contact for id: {id}"}