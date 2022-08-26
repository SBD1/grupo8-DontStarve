#!/bin/sh
# wait-for-postgres.sh
  
until pg_isready -h localhost -p 5432; do
  >&2 echo "Postgres is unavailable - sleeping in" $host:$port
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"
exec "$@"


