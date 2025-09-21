SELECT id, node_type, content, parent_id
FROM WorkflowNodes WHERE workflow_id = (
  SELECT id
  FROM Workflows
  WHERE name = ?
)
