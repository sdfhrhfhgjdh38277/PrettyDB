from prettytable import PrettyTable
from io_operations import save_to_csv, load_from_csv
from loguru import logger
from encryption import *


class CreateTable:
    def __init__(self, field_names):
        self.table = PrettyTable()
        self.table.field_names = [encrypt_data(field) for field in field_names]

    def add_row(self, row):
        if len(row) != len(self.table.field_names):
            logger.error(
                "Error: Count of elements in string does not match the number of fields."
            )
            return
        self.table.add_row([encrypt(item) for item in row])

    def get_decrypted_table(self):
        decrypted_fields = [decrypt_data(field) for field in self.table.field_names]
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
            logger.error(f"Error with download file: {e}")