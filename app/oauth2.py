from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer


# Secret Key 
# Algorithm 
# Expiration Time 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY = '0xc33c3e923bcf7ee9d67fc9c4b860ab9e824898642452d8e074a65df90'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRATION_TIME = 30

# to Generate a Token 
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, details=f"Could not Validate Credentials", headers={'WWW-Authenticate': "Bearer"})

    return verify_access_token(token, credentials_exception)