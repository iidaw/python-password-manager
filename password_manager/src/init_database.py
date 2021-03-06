from database_connection import get_database_connection, get_database_connection_test


def drop_tables(connection):
    """Poistaa tietokantataulut

        Args:
            connection: tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS Passwords;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut

        Args:
            connection: tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE Users (
            username TEXT PRIMARY KEY,
            password TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE Passwords (
            site TEXT,
            username TEXT,
            password TEXT,
            user TEXT,
            FOREIGN KEY(user) REFERENCES Users(username)
        );
    ''')

    connection.commit()


def init_database():
    """Alustaa tietokantataulut"""

    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


def init_database_test():
    """Alustaa tietokantataulut testejä varten"""

    connection_test = get_database_connection_test()
    drop_tables(connection_test)
    create_tables(connection_test)


if __name__ == "__main__":
    init_database()
