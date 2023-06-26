import requests
import pandas as pd
from Extraction.postgres_conn import connection_to_postgres
from Extraction.src.query.create_tags_query import create_tags_query


def fetch_data_from_api(url, params):
    """
    Fetches data from the given API endpoint using the provided parameters.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise exception for non-successful status codes
    data = response.json()
    return data.get('items', [])


def insert_tags_into_database(conn, cursor, tags):
    """
    Insert the fetched tags into the PostgreSQL database.
    """
    for tag in tags:
        insert_query = 'INSERT INTO stackoverflow_tags (name, count) VALUES (%s, %s)'
        cursor.execute(insert_query, (tag['name'], tag['count']))
    conn.commit()


def fetch_and_store_trending_tags(stack_overflow_API: str):
    """
    Fetches and stores trending tags for the month of May 2023 from the Stack Overflow API.
    """
    url = f'{stack_overflow_API}2.3/tags'
    params = {
        'order': 'desc',
        'sort': 'popular',
        'site': 'stackoverflow',
        'pagesize': 50,  # Assuming the requirement of top 50 tags
        "fromdate": "2023-05-01",
        "todate": "2023-05-30"
    }

    try:
        # Create a connection to the PostgreSQL database
        conn = connection_to_postgres()

        # Create a cursor object
        cursor = conn.cursor()

        # Create the table in PostgreSQL if it doesn't exist
        cursor.execute(create_tags_query)

        # Fetch tags from the API
        tags = fetch_data_from_api(url, params)

        # Insert tags into the database
        insert_tags_into_database(conn, cursor, tags)

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
