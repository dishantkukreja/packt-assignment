"""
main.py

This script is the entry point of the project. It extracts data from the Stack Overflow API and stores it in a Postgres database.

Usage:
    python main.py

"""

from Extraction.src.fetch_and_store.asked_questions import fetch_and_store_asked_questions
from Extraction.src.fetch_and_store.get_ans_from_questions import fetch_answers_with_highest_vote
from Extraction.src.fetch_and_store.trending_tags import fetch_and_store_trending_tags
from Extraction.src.fetch_and_store.active_users import fetch_and_store_active_users

stack_overflow_API = "https://api.stackexchange.com/"


def main():
    """Fetches and stores trending tags for the month of May 2023 from the Stack Overflow API."""
    fetch_and_store_trending_tags(stack_overflow_API)

    #Fetches and stores active users from the Stack Overflow API for the past week.
    fetch_and_store_active_users(stack_overflow_API)


    # Fetches and stores question asked with highest score from the Stack Overflow API for the June 2023.
    fetch_and_store_asked_questions(stack_overflow_API)

    # Fetches and stores answers with highest score from the Stack Overflow API for the June 2023.
    fetch_answers_with_highest_vote(stack_overflow_API)


if __name__ == '__main__':
    main()

