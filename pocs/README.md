# POC(s)

### Creating a user

```sh
curl -LX POST --url http://127.0.0.1:8000/api/auth/register \
  -H 'Content-Type: application/json' \
  -d '{"name": "...", "email": "...", "password": "..."}'
```
