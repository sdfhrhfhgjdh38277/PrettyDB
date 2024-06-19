from prettytable import PrettyTable
from .encryption import encrypt, decrypt
from .io import save_to_csv, load_from_csv
from loguru import logger


class CreateTable:
    def __init__(self, field_names):
        self.table = PrettyTable()
        self.table.field_names = [encrypt(field) for field in field_names]

    def add_row(self, row):
        if len(row) != len(self.table.field_names):
            logger.error(
                "Ошибка: количество элементов в строке не совпадает с количеством полей"
            )
            return
        self.table.add_row([encrypt(item) for item in row])

    def get_decrypted_table(self):
        decrypted_fields = [decrypt(field) for field in self.table.field_names]
        decrypted_rows = [[decrypt(item) for item in row] for row in self.table._rows]
        return decrypted_fields, decrypted_rows

    def save_to_file(self, filename):
        save_to_csv(self.table, filename)

    @classmethod
    def load_from_file(cls, filename):
        try:
            field_names, rows = load_from_csv(filename)
            table = cls([decrypt(field) for field in field_names])
            for row in rows:
                table.add_row([decrypt(item) for item in row])
            return table
        except Exception as e:
            logger.error(f"Ошибка при загрузке из файла: {e}")
            return None
