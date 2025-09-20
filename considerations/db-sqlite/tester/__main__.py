import logging
import pathlib
import graphviz

from mapper import SQLMapper


SCHEMA = pathlib.Path("schema.sql").read_text()
DB_FILE = 'example.db'
QUERIES_FOLDER = 'queries'


def create_graph_overview(db):
    db.execute('get_workflow_nodes_by_name', ('Tests',))
    nodes = db.cursor.fetchall()
    print(nodes)

    dot = graphviz.Digraph(name='Tests', format='png')
    dot.attr(rankdir='LR')

    for node_id, node_type, content, parent_id in nodes:
        label = f"{node_type}: {content}"
        dot.node(str(node_id), label)

    for node_id, node_type, content, parent_id in nodes:
        if parent_id is not None:
            dot.edge(str(parent_id), str(node_id))

    dot.render(f"workflow.gv", view=True)


def main():
    logging.basicConfig(level=logging.DEBUG)

    db = SQLMapper(DB_FILE, QUERIES_FOLDER)
    db.cursor.executescript(SCHEMA)

    db.execute('insert_user', ('alice', 'alice@example.com', 'alice_pass'))
    db.execute('insert_user', ('bob', 'bob@example.com', 'bob_pass'))
    db.commit()

    users = db.execute('get_users')
    user_map = {login: user_id for user_id, login in users}

    db.execute('insert_auth_token', (user_map['alice'], 'github', 'repo', 'token_alice_1'))
    db.execute('insert_auth_token', (user_map['alice'], 'slack', 'write', 'token_alice_2'))
    db.execute('insert_auth_token', (user_map['bob'], 'github', 'repo', 'token_bob_1'))
    db.commit()

    db.execute('insert_workflow', ('Tests', 'Simple test workflow'))
    workflow_id = db.cursor.lastrowid

    db.execute('insert_workflow_node', (workflow_id, 'receive', 'foo', None))
    root_id = db.cursor.lastrowid

    db.execute('insert_workflow_node', (workflow_id, 'send', 'bar', root_id))
    child1_id = db.cursor.lastrowid

    db.execute('insert_workflow_node', (workflow_id, 'send', 'baz', root_id))
    db.execute('insert_workflow_node', (workflow_id, 'send', 'qux', child1_id))
    db.commit()

    create_graph_overview(db)
    db.close()


if __name__ == '__main__':
    main()
