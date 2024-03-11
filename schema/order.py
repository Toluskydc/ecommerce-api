from pydantic import BaseModel
from enum import Enum
from schema.product import Product

# > 4... Order status Added to order entity
class OrderStatus(Enum):
    completed = "COMPLETED"
    pending = "PENDING"
print(OrderStatus.completed.value)

stat = OrderStatus.completed.value

class Order(BaseModel):
    id: int
    customer_id: int
    items: list[int]
    status: str = OrderStatus.pending.value

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]                           

orders = [
    Order(id=1, customer_id=1, items=[1, 2], status= "pending")
]