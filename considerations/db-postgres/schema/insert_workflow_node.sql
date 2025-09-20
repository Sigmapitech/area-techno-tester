INSERT INTO WorkflowNodes (workflow_id, node_type, content, parent_id)
VALUES ($1, $2, $3, $4)
RETURNING id;
