rm -rf db
mkdir -p db

mongod --dbpath db &
MONGO_PID=$!

python populate.py
python dot.py

kill $MONGO_PID
wait $MONGO_PID 2>/dev/null
