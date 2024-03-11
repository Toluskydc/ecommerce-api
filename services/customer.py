from fastapi import HTTPException

from schema.customer import customers, CustomerCreate, Customer

#1 > a dependency that checks that a username is not in the system when creating a customer.
# > making sure Usernames are unique
class CustomerService:
    @staticmethod
    def is_username_unique(payload: CustomerCreate):
        for customer in customers:
            if customer.username == payload.username:
                raise HTTPException(status_code=400, detail=f'customer with username {payload.username} already exists')
        return payload
            


customer_service = CustomerService()