create_questions_query = '''CREATE TABLE IF NOT EXISTS stackoverflow_questions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    question_id INT,
    score INT,
    title VARCHAR(255),
    link varchar(255)
      )'''