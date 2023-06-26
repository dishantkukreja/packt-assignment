create_users_query = """
CREATE TABLE IF NOT EXISTS StackOverflowUsers (
    id SERIAL PRIMARY KEY,
    account_id INT,
    display_name VARCHAR(255),
    reputation INT
)
"""