from graphviz import Digraph
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from schema import Base, User, AuthToken, Workflow, WorkflowNode


def main():
    engine = create_engine('mysql+pymysql://root:@localhost:3306/db_name', echo=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    alice = User(login='alice', email='alice@example.com', authentication_string='alice_pass')
    bob = User(login='bob', email='bob@example.com', authentication_string='bob_pass')
    session.add_all([alice, bob])
    session.commit()

    alice.tokens = [
        AuthToken(service='github', scope='repo', token='token_alice_1'),
        AuthToken(service='slack', scope='write', token='token_alice_2')
    ]

    bob.tokens = [AuthToken(service='github', scope='repo', token='token_bob_1')]
    session.commit()

    workflow = Workflow(name='Tests', description='Simple test workflow')
    session.add(workflow)
    session.commit()

    root = WorkflowNode(workflow=workflow, node_type='receive', content='foo')
    child1 = WorkflowNode(workflow=workflow, node_type='send', content='bar', parent=root)
    child2 = WorkflowNode(workflow=workflow, node_type='send', content='baz', parent=root)
    child3 = WorkflowNode(workflow=workflow, node_type='send', content='qux', parent=child1)

    session.add_all([root, child1, child2, child3])
    session.commit()

    workflows = session.query(Workflow).all()

    for workflow in workflows:
        dot = Digraph(name=workflow.name, format='png')
        dot.attr(rankdir='LR')

        for node in workflow.nodes:
            label = f"{node.node_type}: {node.content}"
            dot.node(str(node.id), label)

        for node in workflow.nodes:
            if node.parent_id:
                dot.edge(str(node.parent_id), str(node.id))

        filename = f"workflow_{workflow.name}.gv"
        dot.render(filename, view=True)


if __name__ == "__main__":
    main()
