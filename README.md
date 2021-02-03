# Django Docker + Github Action
## Components
- alpine mariadb server
- alpine redis server 
- alpine nginx server
- alpine miniconda3  

## Scheme
- mysql data: $HOME/data/production_db
- redis data: $HOME/data/production_redis
- static data: $HOME/data/production_static
- django script/app top level folder: $HOME/django_app

## Github Action
- When push to main detected, it will fetch latest commit, and rebuild/restart the docker-compose daemon

## Howto (Github Action)
- Create a gcp or ec2 container
- Install docker.io and docker-compose in container
- Set action from repo->settings, add runner
- Follow the steps by steps in the container
- Prepare the django_app in $HOME/django_app
  - *NOTE* 
    - use 'redis' as redis host if use internal redis cache
    - use 'db' as mysql host if use internal mysql/mariadb server
- Create a .live.env in $HOME/django_app
  - MYSQL_DATABASE=dbname
  - MYSQL_ROOT_PASSWORD=root_password
  - MYSQL_USER=user_db
  - MYSQL_PASSWORD=user_pw
  - VERSION=devel
  - DJANGO_APP_SECRET_KEY=random
  - DOMAIN=beta.dermai.com.tw
- Clone this repo to $HOME/docker-django
- Do the push/commit to main to trigger the flow
- Add superuser: exec -it <id of django-calendar_app> /app/manage.py createsuperuser
- Access django admin: https:<DOMAIN>/admin
- Access django shell: exec -it <id of django-calendar-app> /app/manage.py shell_plus

## TODO
- [v] Add github action rebuilding image
- [v] Add DNS/SSL to the flow
- [ ] Add django superuser on the first deploy
