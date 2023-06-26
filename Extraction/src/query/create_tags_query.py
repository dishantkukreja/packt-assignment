create_tags_query = '''
CREATE TABLE IF NOT EXISTS stackoverflow_tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    count INT
  )
'''