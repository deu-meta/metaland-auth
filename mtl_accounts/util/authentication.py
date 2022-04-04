import os
from time import time
from typing import Dict

import jwt
from fastapi import HTTPException, Request
from starlette.responses import JSONResponse

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_jwt(user: Dict, expiraton: int) -> Dict[str, str]:
    expires = {"exp": time() + expiraton}
    payload = dict(user, **expires)

    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return token


async def decode_jwt(access_token):
    access_token = access_token.replace("Bearer ", "")
    payload = jwt.decode(jwt=access_token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return payload
