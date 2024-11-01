include .env

build: # Build the docker images
	docker compose build

up: 
	docker compose up -d

down: 
	docker compose down

restart: 
	make down && make up

to_psql: 
	docker exec -ti de_psql psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

to_mysql: #
	docker exec -it de_mysql mysql --local-infile=1 -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" ${MYSQL_DATABASE}

to_mysql_root: # Connect to the MySQL container as root
	docker exec -it debezium_mysql mysql -u"root" -p"${MYSQL_ROOT_PASSWORD}" ${MYSQL_DATABASE}