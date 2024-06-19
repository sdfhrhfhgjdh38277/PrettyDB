from cryptography.fernet import Fernet
from loguru import logger

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(data):
    try:
        return cipher_suite.encrypt(data.encode()).decode()
    except Exception as e:
        logger.error(f"Ошибка при шифровании данных: {e}")
        return None

def decrypt(data):
    try:
        return cipher_suite.decrypt(data.encode()).decode()
    except Exception as e:
        logger.error(f"Ошибка при дешифровании данных: {e}")
        return None