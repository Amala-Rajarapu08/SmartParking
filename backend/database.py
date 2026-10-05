import sqlite3


DATABASE_NAME = "parking.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS parking_slots (
            slot_number INTEGER PRIMARY KEY,
            vehicle_number TEXT
        )
    """
    )

    # Create 5 parking slots if they don't already exist
    for slot in range(1, 6):
        cursor.execute(
            """
            INSERT OR IGNORE INTO parking_slots
            (slot_number, vehicle_number)
            VALUES (?, NULL)
            """,
            (slot,),
        )

    connection.commit()
    connection.close()


def get_all_slots():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT slot_number, vehicle_number
        FROM parking_slots
        ORDER BY slot_number
    """
    )

    rows = cursor.fetchall()

    connection.close()

    return {row["slot_number"]: row["vehicle_number"] for row in rows}


def park_vehicle(slot_number, vehicle_number):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE parking_slots
        SET vehicle_number = ?
        WHERE slot_number = ?
        """,
        (vehicle_number, slot_number),
    )

    connection.commit()
    connection.close()


def remove_vehicle(slot_number):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE parking_slots
        SET vehicle_number = NULL
        WHERE slot_number = ?
        """,
        (slot_number,),
    )

    connection.commit()
    connection.close()
