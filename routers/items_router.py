from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated 
from sqlmodel import Session, select
from configs.database import get_session
from models.item_model import ItemsModel

items_router = APIRouter(tags=['items'])

SessionDep = Annotated[Session, Depends(get_session)]

@items_router.get("/items", name='Get all items')
def get_items(session: SessionDep):
    items = session.exec(select(ItemsModel)).all()
    return items

@items_router.get("/items/{item_id}", name='Get item')
def read_item(item_id: int, item: ItemsModel, session: SessionDep):
    item = session.get(item, item_id)
    if item:
        return item
    return {"error": "Item not found"}

@items_router.post("/add_items", name='Create item')
async def create_item(item: ItemsModel, session: SessionDep) -> ItemsModel:
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@items_router.delete("/delete_item/{item_id}", name='Delete item')
def delete_item(item_id: int, item: ItemsModel, session: SessionDep):
    item = session.get(ItemsModel, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(item)
    session.commit()
    return {"ok": True}