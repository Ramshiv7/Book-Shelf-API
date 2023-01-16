from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash_pass(pwd: str):
    return pwd_context.hash(pwd)


def verify_pwd(plain_pass, hashed_password):
    return pwd_context.verify(plain_pass, hashed_password)