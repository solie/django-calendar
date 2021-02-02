# Django Docker + Github Action
## Components
- alpine mariadb server
- alpine redis server 
- alpine nginx server
- alpine miniconda3  

## Scheme
- mysql data: data/production_db
- redis data: data/production_redis
- static data: data/production_static
- django script/app top level folder: src

## Build images & Running
- docker-compose build (only when requirements.txt/domain name changed)
- docker-compose up/start/restart

## Github Action
- When push to main detected, it will fetch latest commit, and rebuild/restart the docker-compose daemon

## Howto
- Create a gcp or ec2 container
- Install docker.io and docker-compose in container
- Set action from repo->settings, add runner
- Follow the steps by steps in the container
- Do the push/commit to main to trigger the flow
- Check running service: http://<container_ip>/
- Add superuser: exec -it <id of django-calendar_app> /app/manage.py createsuperuser
- Access django admin: http:<container_ip>/admin
- Access django shell: exec -it <id of django-calendar-app> /app/manage.py shell_plus
- Live demo: http://mauu.ga/

## TODO
- [v] Add github action rebuilding image
- [ ] Add DNS/SSL to the flow
