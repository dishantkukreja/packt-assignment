import requests
import psycopg2
import json
from Extraction.postgres_conn import connection_to_postgres
from Extraction.src.query.create_ans_query import create_ans_query
from .trending_tags import fetch_data_from_api


def insert_answers_into_database(conn, cursor, answers):
    """
    Insert the fetched answers into the PostgreSQL database.
    """
    for answer in answers:
        answer_id = answer.get('answer_id')
        score = answer.get('score')
        owner = answer.get('owner', {})
        owner_json = json.dumps(owner)  # Convert owner dictionary to JSON string
        insert_query = 'INSERT INTO stackoverflow_answers (answer_id, score, owner) VALUES (%s, %s, %s)'
        cursor.execute(insert_query, (answer_id, score, owner_json))
    conn.commit()


def fetch_answers_with_highest_vote(stack_overflow_API: str):
    """
    Fetches and stores answers from the Stack Overflow API with the highest votes within a specific date range.
    """
    url = f'{stack_overflow_API}2.3/answers'
    params = {
        'order': 'desc',
        'sort': 'votes',
        'site': 'stackoverflow',
        'pagesize': 50,  # Number of answers to fetch
        'fromdate': '2022-06-01',
        'todate': '2022-06-30'
    }

    try:
        # Create a connection to the PostgreSQL database
        conn = connection_to_postgres()

        # Create a cursor object
        cursor = conn.cursor()

        # Create the table in PostgreSQL if it doesn't exist
        cursor.execute(create_ans_query)

        # Fetch answers from the API
        answers = fetch_data_from_api(url, params)

        # Insert answers into the database
        insert_answers_into_database(conn, cursor, answers)

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
