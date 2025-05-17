from functools import wraps
from typing import Callable, TypeVar
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from app.core.exceptions import DatabaseError, NotFoundError

T = TypeVar("T")


def handle_db_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except NoResultFound:
            raise NotFoundError()
        except SQLAlchemyError as e:
            if hasattr(args[0], "session"):
                await args[0].session.rollback()
            raise DatabaseError(str(e))

    return wrapper
