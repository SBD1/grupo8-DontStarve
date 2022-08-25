docker rm -f $(docker ps -a -q)
docker-compose up db -d
sleep 2
docker-compose run dontstarve