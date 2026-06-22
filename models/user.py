from sqlalchemy import BigInteger, Column, String, Text

from config import database

class User(database.Model):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    # 存储请求方用于与提供方通信的公钥
    public_key = Column(Text, nullable=False)
