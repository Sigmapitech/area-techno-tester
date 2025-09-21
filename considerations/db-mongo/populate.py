from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['workflow_db']

users_col = db['Users']
tokens_col = db['AuthTokens']
workflows_col = db['Workflows']
nodes_col = db['WorkflowNodes']

alice_id = users_col.insert_one({
    "login": "alice",
    "email": "alice@example.com",
    "authentication_string": "alice_pass"
}).inserted_id

bob_id = users_col.insert_one({
    "login": "bob",
    "email": "bob@example.com",
    "authentication_string": "bob_pass"
}).inserted_id

tokens_col.insert_many([
    {"user_id": alice_id, "service": "github", "scope": "repo", "token": "token_alice_1"},
    {"user_id": alice_id, "service": "slack", "scope": "write", "token": "token_alice_2"},
    {"user_id": bob_id, "service": "github", "scope": "repo", "token": "token_bob_1"}
])

workflow_id = workflows_col.insert_one({
    "name": "Tests",
    "description": "Simple test workflow"
}).inserted_id

root_id = nodes_col.insert_one({
    "workflow_id": workflow_id,
    "node_type": "receive",
    "content": "foo",
    "parent_id": None
}).inserted_id

child1_id = nodes_col.insert_one({
    "workflow_id": workflow_id,
    "node_type": "send",
    "content": "bar",
    "parent_id": root_id
}).inserted_id

child2_id = nodes_col.insert_one({
    "workflow_id": workflow_id,
    "node_type": "send",
    "content": "baz",
    "parent_id": root_id
}).inserted_id

nodes_col.insert_one({
    "workflow_id": workflow_id,
    "node_type": "send",
    "content": "qux",
    "parent_id": child1_id
})

print("Populated successfully")
