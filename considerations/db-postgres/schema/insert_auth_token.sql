INSERT INTO AuthTokens (user_id, service, scope, token)
VALUES ($1, $2, $3, $4)
RETURNING id;
