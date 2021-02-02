# Django Docker + Github Action
## Components
- alpine mariadb server
- alpine redis server 
- alpine nginx server
- alpine miniconda3  

## Scheme
- mysql data: production_db
- redis data: production_redis
- static data: production_static
- django script/app top level folder: src

## Build images & Running
- docker-compose build (only when requirements.txt/domain name changed)
- docker-compose up/start/restart

## Github Action
- When push to main detected, it will fetch latest commit

## TODO
[ ] Add github action rebuilding image
