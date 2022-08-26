docker rm -f $(docker ps -a --filter "name=grupo8-dontstarve" -q)
docker-compose up -d db
docker-compose build dontstarve
./wait-for-postgres.sh
docker-compose run dontstarve
docker-compose stop
