from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from database import Base


class Order(Base, SerializerMixin):
    tablename = "orders"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    '''password = Column(String)  # hashed password
    is_active = Column(Boolean, default=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, index=True)
    email_confirmed = Column(Boolean, default=False)
    certificates = relationship("Certificate", back_populates="user")'''

    # items = relationship("Item", back_populates="owner")