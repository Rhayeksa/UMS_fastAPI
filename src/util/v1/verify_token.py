import jwt

from src.config import JWT_ALGORITHM, JWT_SECRET_KEY


def f(token: str):
    try:
        return jwt.decode(
            jwt=token,
            key=JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )
    except jwt.ExpiredSignatureError:
        # Terjadi jika waktu 'exp' sudah terlampaui
        return "TOKEN_EXPIRED"
    except jwt.InvalidTokenError:
        # Terjadi jika signature salah, format rusak, atau manipulasi lainnya
        return "INVALID_TOKEN"
