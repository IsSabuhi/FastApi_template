from sqlmodel import Field, SQLModel
from typing import Union

class ItemsModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None, index=True)
    price: float
    tax: Union[float, None] = None