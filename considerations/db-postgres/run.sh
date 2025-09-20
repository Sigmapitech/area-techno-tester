export PGDATA="$PWD/pgdata"
export PGSOCKET="$PWD/pgsocket"

rm -rf "$PGDATA"

mkdir -p "$PGDATA"
mkdir -p "$PGSOCKET"

initdb $PGDATA

pg_ctl -D $PGDATA -o "-p 5432 -k $PGSOCKET" start
python tester
