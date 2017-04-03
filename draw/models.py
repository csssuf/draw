from sqlalchemy import Column, String, Integer
from draw.database import Base

class User(Base):
    __tablename__ = "User"
    username = Column(String(60), primary_key=True)
    code = Column(String(1024))
    refresh_token = Column(String(1024), nullable=True)
    seconds_left = Column(Integer)

    def __init__(self, _username, _code, _refresh):
        self.username = _username
        self.code = _code
        self.refresh_token = _refresh
        self.seconds_left = 300
