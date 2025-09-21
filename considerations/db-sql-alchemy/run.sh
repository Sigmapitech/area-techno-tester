rm -rf .mysql

export MYSQL_HOME=$PWD/.mysql
export MYSQL_DATADIR=$MYSQL_HOME/data

export MYSQL_UNIX_PORT=$MYSQL_HOME/mysql.sock
export MYSQL_PID_FILE=$MYSQL_HOME/mysql.pid

mysql_install_db --auth-root-authentication-method=normal \
  --datadir=$MYSQL_DATADIR --basedir=$MYSQL_BASEDIR       \
  --pid-file=$MYSQL_PID_FILE

mariadbd \
  --datadir="$MYSQL_DATADIR"   \
  --pid-file="$MYSQL_PID_FILE" \
  --socket="$MYSQL_UNIX_PORT" &

MARIA_PID=$!

sleep 2
echo "CREATE DATABASE IF NOT EXISTS db_name" | mysql -u root

python tester

kill $MARIA_PID
wait $MARIA_PID 2>/dev/null
