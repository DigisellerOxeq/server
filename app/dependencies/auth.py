from fastapi import Header, HTTPException, status

from app.core.config import settings


def get_auth(
        token: str = Header(alias='x-auth-token')
    ) -> str:
    if token != settings.auth.token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid token'
        )
    return token
