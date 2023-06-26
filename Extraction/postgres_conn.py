import psycopg2


def connection_to_postgres():
    """Establishes a connection to the PostgreSQL database and returns the connection object."""

    db_host = 'localhost'
    db_name = 'postgres'
    db_user = 'user_d'
    db_password = 'password_d'

    try:
        conn = psycopg2.connect(
            host=db_host,
            port=5432,
            dbname=db_name,
            user=db_user,
            password=db_password
        )

        return conn

    except psycopg2.Error as e:
        print(f"Error occurred while connecting to the PostgreSQL database: {str(e)}")
        return None
