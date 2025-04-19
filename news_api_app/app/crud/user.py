from sqlalchemy.orm import Session
from app.models.user import UserDB

def get_user(db: Session, username: str):
    return db.query(UserDB).filter(UserDB.username == username).first()

def create_user(db: Session, user_data: dict):
    user = UserDB(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
