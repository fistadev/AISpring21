# import models
# from utils.db.connect import HOST

# print(HOST)


from utils.db.connect import db_engine
from utils.db.models.user import User
from sqlalchemy.orm import Session

# db instance
engine = db_engine()

# session instance
session = Session(engine, future=True)


def create_user(name, last_name, email, password_hash):
    user = User(
        name=name, last_name=last_name, email=email, password_hash=password_hash
    )
    session.add(user)
    session.commit()
    return user.toJSON()


def get_users():
    result = [row.toJSON() for row in session.query(User)]
    return result


def get_users_by_id(id):
    user = session.query(User).get(id)
    if user:
        return user.toJSON()
    return None


def update_user_by_id(id, update):
    user = session.query(User).get(id)
    if user:
        for key, value in update.items():
            setattr(user, key, value)
        session.commit()
        return user.toJSON()
    return None


def delete_user_by_id(id):
    user = session.query(User).get(id)
    if user:
        session.delete(user)
        session.commit()
        return user.toJSON()
    return None


# create_user('Fabio', 'Fistarol', 'fistadev@gmail.com', '11223344')
