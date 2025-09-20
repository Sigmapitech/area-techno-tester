INSERT INTO Users (login, email, authentication_string)
VALUES ($1, $2, $3)
RETURNING id;
