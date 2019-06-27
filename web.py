from flask import Flask
from web.model import DbPool, User

app = Flask(__name__)

if __name__ == '__main__':
    session = DbPool.get_db_pool1()()
    user = User(id='1', name='alan')
    session.add(user)
    session.commit()
    session.close()
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
