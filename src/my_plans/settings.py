from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite3'

    jwt_secret: str = 'mAhrYw_9DiNE9cgu9JkRhfKJ_CCbd9Q4al0GowIBdk4'  # Секретный ключ / Лучше конечно вынести в .env
    jwt_algorithm: str = 'HS256'  # Алгоритм шифрования
    jwt_expiration: int = 60000  # Время жизни токена


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
