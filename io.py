import csv
from loguru import logger

def save_to_csv(table, filename):
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(table.field_names)
            writer.writerows(table._rows)
    except Exception as e:
        logger.error(f"Ошибка при сохранении в файл: {e}")

def load_from_csv(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            field_names = next(reader)
            rows = [row for row in reader]
        return field_names, rows
    except Exception as e:
        logger.error(f"Ошибка при загрузке из файла: {e}")
        return None, None