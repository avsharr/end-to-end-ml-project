import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"

# 1. Путь только до папки logs (без имени файла)
logs_path = os.path.join(os.getcwd(), "logs")

# 2. Создаем папку logs
os.makedirs(logs_path, exist_ok=True)

# 3. Полный путь к файлу (папка + файл)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging started")
