# flask-sqlalchemy
简单的单例的

绑定的对象一定是SQLAlchemy engine，不可以是MySQLDb connection
SessionFactory = sessionmaker(bind=engine)
