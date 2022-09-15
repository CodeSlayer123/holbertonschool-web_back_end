#!/usr/bin/env python3
"""task 0 task 0 task 0 task 0 task 0 task 0"""

from ast import get_docstring
from typing import List
import re
import logging
import sys
import mysql.connector
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """task 0 task 0 task 0 task 0 task 0 task 0"""
    need_to_be_redacted = filter_datum_splitter(fields, message, separator)
    result = message
    for j in need_to_be_redacted:
        result = re.sub(j, redaction + separator, result)
    return result


def filter_datum_splitter(fields: List[str], message: str,
                          separator: str) -> List[str]:
    """splits message by equal sign and returns list of
    each value that needs to be redacted"""
    need_to_be_redacted = []
    individual_fields = message.split(separator)
    for i in individual_fields:
        if (len(i) > 0):
            x = i.split("=")
            key = x[0]
            value = x[1]
        if (key in fields and value not in need_to_be_redacted):
            need_to_be_redacted.append(value + separator)
    return need_to_be_redacted


def get_logger() -> logging.Logger:
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(ch)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(
        host=os.environ.get("PERSONAL_DATA_DB_HOST"),
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD"),
        database=os.environ.get("PERSONAL_DATA_DB_NAME")
        )


def main():
    log = get_logger()
    my_db = get_db()
    cursor = my_db.cursor(dictionary=True)
    query = "SELECT * FROM users;"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        for key, value in row.items():
            my_format = "; ".join(f"{key}={value}")
            log.warning(my_format)
    my_db.close()

if __name__ == "__main__":
    main()
