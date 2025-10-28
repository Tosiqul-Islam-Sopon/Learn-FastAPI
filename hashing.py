from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)