import psycopg2
import requests
from Extraction.postgres_conn import connection_to_postgres
from Extraction.src.query.create_question_query import create_questions_query
from .trending_tags import fetch_data_from_api


def insert_questions_into_database(conn, cursor, questions):
    """
    Insert the fetched questions into the PostgreSQL database.
    """
    for question in questions:
        owner = question.get('owner', {})
        user_id = owner.get('user_id', None)
        insert_query = 'INSERT INTO stackoverflow_questions (user_id, question_id, score, title, link) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(insert_query, (user_id, question['question_id'], question['score'], question['title'], question['link']))
    conn.commit()


def fetch_and_store_asked_questions(stack_overflow_API: str):
    """
    Fetches questions with high votes from the Stack Overflow API and stores them in the PostgreSQL database.
    """
    url = f'{stack_overflow_API}2.3/questions'
    params = {
        'order': 'desc',
        'sort': 'votes',
        'site': 'stackoverflow',
        'pagesize': 50,
        'fromdate': '2022-06-01',
        'todate': '2022-06-30'
    }

    try:
        # Create a connection to the PostgreSQL database
        conn = connection_to_postgres()

        # Create a cursor object
        cursor = conn.cursor()

        # Create the table in PostgreSQL if it doesn't exist
        cursor.execute(create_questions_query)

        # Fetch questions from the API
        questions = fetch_data_from_api(url, params)

        # Insert questions into the database
        insert_questions_into_database(conn, cursor, questions)

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
