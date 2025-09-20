import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

with open('schema.sql', 'r') as f:
    schema_sql = f.read()

cursor.executescript(schema_sql)

cursor.execute(
    "INSERT INTO Users (login, email, authentication_string) VALUES (?, ?, ?)",
    ('alice', 'alice@example.com', 'alice_pass'))
cursor.execute(
    "INSERT INTO Users (login, email, authentication_string) VALUES (?, ?, ?)",
    ('bob', 'bob@example.com', 'bob_pass'))

cursor.execute("SELECT id, login FROM Users")
users = {login: user_id for user_id, login in cursor.fetchall()}

tokens = [
    (users['alice'], 'github', 'repo', 'token_alice_1'),
    (users['alice'], 'slack', 'write', 'token_alice_2'),
    (users['bob'], 'github', 'repo', 'token_bob_1')
]
cursor.executemany(
    "INSERT INTO AuthTokens (user_id, service, scope, token) VALUES (?, ?, ?, ?)",
    tokens)

cursor.execute(
    "INSERT INTO Workflows (name, description) VALUES (?, ?)",
    ('Tests', 'Simple test workflow'))

workflow_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO WorkflowNodes (workflow_id, node_type, content, parent_id) VALUES (?, ?, ?, ?)",
    (workflow_id, 'receive', 'foo', None))
root_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO WorkflowNodes (workflow_id, node_type, content, parent_id) VALUES (?, ?, ?, ?)",
    (workflow_id, 'send', 'bar', root_id))
child1_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO WorkflowNodes (workflow_id, node_type, content, parent_id) VALUES (?, ?, ?, ?)",
    (workflow_id, 'send', 'baz', root_id))
child2_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO WorkflowNodes (workflow_id, node_type, content, parent_id) VALUES (?, ?, ?, ?)",
    (workflow_id, 'send', 'qux', child1_id))

conn.commit()
conn.close()

print("Database populated successfully!")
