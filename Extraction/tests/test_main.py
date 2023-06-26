import pytest
import psycopg2
from unittest.mock import Mock, patch
from Extraction.postgres_conn import connection_to_postgres
from Extraction.src.fetch_and_store.trending_tags import fetch_data_from_api
from requests.exceptions import HTTPError


def test_connection_to_postgres():
    conn = connection_to_postgres()
    assert conn is not None
    conn.close()

def test_fetch_tags_from_api_exception(mocker):
    # Create a mocker instance
    mock = mocker.patch('requests.get')

    # Configure the mock to raise an exception
    mock.side_effect = HTTPError("API Error")

    # Define the test URL and parameters
    url = "https://api.example.com/tags"
    params = {
        "order": "desc",
        "sort": "popular",
        "site": "example",
        "pagesize": 5
    }

    # Assert that the function raises the expected exception
    with pytest.raises(HTTPError):
        fetch_data_from_api(url, params)