docker-compose up -d db
./wait-for-postgres.sh
docker-compose build dontstarve
docker-compose run --service-ports dontstarve python main.py bash
docker-compose stop