
from starlette.config import Config


config = Config("venv")
URL = "postgresql://postgres:jango@localhost:5432/pharmacy"
DATABASE_URL = URL
ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = '8d81e3a0392182ca9af1d1bd94e9ff8d129be254ab7a83f1f2e259dc3b7f84ac'
ALGORITHM = "HS256"