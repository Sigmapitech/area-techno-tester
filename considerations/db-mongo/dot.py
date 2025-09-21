from pymongo import MongoClient
from graphviz import Digraph

client = MongoClient("mongodb://localhost:27017/")
db = client['workflow_db']

workflows = list(db['Workflows'].find({}))

for workflow in workflows:
    workflow_id = workflow['_id']
    workflow_name = workflow['name']
    print(f"Workflow: {workflow_name}")

    nodes = list(db['WorkflowNodes'].find({"workflow_id": workflow_id}))

    dot = Digraph(name=workflow_name, format='png')
    dot.attr(rankdir='LR')

    for node in nodes:
        label = f"{node['node_type']}: {node['content']}"
        dot.node(str(node['_id']), label)

    for node in nodes:
        parent_id = node.get('parent_id')
        if parent_id:
            dot.edge(str(parent_id), str(node['_id']))

    dot.render(f"workflow_{workflow_name}.gv", view=True)
