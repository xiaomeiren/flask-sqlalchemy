from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import threading
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'web'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


class DbPool(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        if not hasattr(DbPool, "pool"):
            DbPool.get_db_pool1()
        else:
            pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(DbPool, "_instance"):
            with DbPool._instance_lock:
                if not hasattr(DbPool, "_instance"):
                    DbPool._instance = object.__new__(cls, *args, **kwargs)
        return DbPool._instance

    @staticmethod
    def get_db_pool1():
        engine = create_engine(
            "mysql+cymysql://root:123456@localhost:3306/web",
            max_overflow=0,  # 超过连接池大小外最多创建的连接
            pool_size=5,  # 连接池大小
            pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
            pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        )
        SessionFactory = sessionmaker(bind=engine)
        session = scoped_session(SessionFactory)
        return session
