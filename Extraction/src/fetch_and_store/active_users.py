import time
import requests
from Extraction.postgres_conn import connection_to_postgres
from Extraction.src.query.create_users_query import create_users_query
from .trending_tags import fetch_data_from_api


def insert_users_into_database(conn, cursor, users):
    """
    Insert the fetched users into the PostgreSQL database.
    """
    for user in users:
        insert_query = 'INSERT INTO StackOverflowUsers (account_id, display_name, reputation) VALUES (%s, %s, %s)'
        cursor.execute(insert_query, (user['account_id'], user['display_name'], user['reputation']))
    conn.commit()


def fetch_and_store_active_users(stack_overflow_API):
    """
    Fetches and stores active users from the Stack Overflow API for the past week.
    """
    url = f'{stack_overflow_API}2.3/users'
    params = {
        'order': 'desc',
        'sort': 'reputation',
        'site': 'stackoverflow',
        'pagesize': 50,  # Assuming the requirement of top 50 active users
        'fromdate': int(time.time()) - 604800  # Fetch top 50 active users in the last week (604800 seconds)
    }

    try:
        # Create a connection to the PostgreSQL database
        conn = connection_to_postgres()

        # Create a cursor object
        cursor = conn.cursor()

        # Create the table in PostgreSQL if it doesn't exist
        cursor.execute(create_users_query)

        # Fetch users from the API
        users = fetch_data_from_api(url, params)

        # Insert users into the database
        insert_users_into_database(conn, cursor, users)

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making a request to the Stack Overflow API: {str(e)}")
        return None
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error occurred while processing the response data: {str(e)}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
