create_ans_query = '''CREATE TABLE IF NOT EXISTS stackoverflow_answers (
    id SERIAL PRIMARY KEY,
    answer_id BIGINT ,
    score INTEGER,
    owner JSONB
)'''