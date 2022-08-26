docker rm -f $(docker ps -a -q)
docker-compose up -d db
docker-compose build dontstarve
./wait-for-postgres.sh
docker-compose run dontstarve
docker-compose stop
