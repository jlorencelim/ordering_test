# ordering_test

## To start development:
1. install [docker](https://docs.docker.com/#/components) and [docker-compose](https://docs.docker.com/compose/install/)
2. clone this repository
3. run `docker-compose build` to build web container
4. run `docker-compose up web` to test web and db containers
5. `sudo docker exec -it ordering_test_web_1 "bash"`
6. `python3 manage.py migrate`
7. `python3 manage.py createsuperuser`

## To run project:
1. run `docker-compose up web`
2. point your browser to `localhost:8000`
3. press `CTRL+C` to stop

## Access to sql server
1. sudo docker-compose run db sqlcmd -S db1.internal.prod.example.com -U SA -P 'Alaska2017' -Q 'select 1'
