from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Key(Base):
    __tablename__ = "keys"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    redeemed = Column(Boolean, default=False)
    hwid = Column(String, nullable=True)
    user = Column(String, nullable=True)
