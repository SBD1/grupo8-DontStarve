docker-compose up -d db
docker-compose build dontstarve
./wait-for-postgres.sh
docker-compose run --service-ports dontstarve python main.py bash
docker-compose stop
docker-compose down --volumes
