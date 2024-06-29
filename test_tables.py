from loguru import logger

try:
    from PrettyDB import *
except:
    logger.critical("Import error")
import unittest
from unittest import TestCase

def test(TestCase):
    table = CreateTable(["Name", "Age"])
    table.add_row(["Alice", 30])
    table.add_row(["Bob", 25])

    fields, rows = table.get_decrypted_table()
    print("Fields:", fields)
    print("Rows:", rows)

if __name__ == "__main__":
    unittest.main(test)