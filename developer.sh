docker-compose down --volumes
docker rm -f $(docker ps -a --filter "name=grupo8-dontstarve" -q)
docker-compose up -d db
docker-compose build dontstarve
./wait-for-postgres.sh
docker-compose run --service-ports dontstarve python main.py bash
docker-compose stop
