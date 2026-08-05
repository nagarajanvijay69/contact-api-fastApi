from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from database import Base, engine, Session, get_db
from schemas import ContactCreate, ContactUpdate, ContactResponse
from models import Contact
from sqlalchemy import select

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/contacts")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = Contact(
       name=contact.name,
       email=contact.email,
       phone=contact.phone
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return {
        "success": True,
        "message": "Contact Created!",
        "contact": new_contact
    }


@app.get("/contacts")
def get_contacts(db: Session = Depends(get_db)):
    statement = select(Contact)
    result = db.execute(statement=statement)
    contacts = result.scalars().all()
    return contacts


@app.put("/contacts/{id}", response_model=ContactResponse)
def update_contact(id: int, contact: ContactUpdate, db: Session = Depends(get_db),):
    statement = select(Contact).where(Contact.id == id)
    result = db.execute(statement=statement)

    existing_contact = result.scalars().first()

    if existing_contact is None:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )

    if contact.name is not None:
        existing_contact.name = contact.name
    if contact.email is not None:    
        existing_contact.email = contact.email
    if contact.phone is not None:    
        existing_contact.phone = contact.phone

    db.commit()
    db.refresh(existing_contact)
    print(existing_contact)
    return existing_contact


@app.delete("/contacts/{id}")
def delete_contact(id: int, db: Session = Depends(get_db)):

    statement = select(Contact).where(Contact.id == id)
    result = db.execute(statement=statement)
    
    existing_contact = result.scalars().first()
    
    if existing_contact is None:
        raise HTTPException(
                status_code=404,
                detail="user not found"
        )
    db.delete(existing_contact)
    db.commit()
    return {
        "message": "Deleted Successfully"
    }