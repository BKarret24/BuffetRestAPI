from sqlalchemy.orm import Session

from models.orders import Order


def get_orders(user_name: str, db: Session):
    orders = db.query(Order).first()
    print(orders)
    return orders


def user_add(order: Order, db: Session):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
