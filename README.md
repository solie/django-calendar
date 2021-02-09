# Django Docker + Github Action
## Components
- alpine mariadb server
- alpine redis server 
- alpine nginx server
- alpine miniconda3
- alpine Caddy v2

## Scheme
- mysql data: $DATA_DIR/production_db
- redis data: $DATA_DIR/redis_data
- static data: $DATA_DIR/production_static
- Django app: $PWD/django_app (can use link, e.g: `ln -s ~/django_project ./django_app`)
- Caddy data: $DATA_DIR/caddy_data & caddy_config

## Github Action
- Set DATA_DIR outside of $PWD, since it will be replace on every action, eg:
$HOME/data
- When push to main detected, it will fetch latest commit, and rebuild/restart the docker-compose daemon

## Howto (Github Action)
- Create a gcp or ec2 container
- Install docker.io and docker-compose in container
- Set action from repo->settings, add runner
- Follow the steps by steps in the container
- Clone this repo to $HOME/docker-django
- Prepare the django_app in django-docker/django_app
  - *NOTE* 
    - use 'redis' as redis host if use internal redis cache
    - use 'db' as mysql host if use internal mysql/mariadb server
- Create a .env in $PWD
  - MYSQL_DATABASE=dbname
  - MYSQL_ROOT_PASSWORD=root_password
  - MYSQL_USER=user_db
  - MYSQL_PASSWORD=user_pw
  - VERSION=devel
  - DJANGO_APP_SECRET_KEY=random
  - DOMAIN=beta.dermai.com.tw
- Do the push/commit to main to trigger the flow
- Add superuser: exec -it <id of django-calendar_app> /app/manage.py createsuperuser
- Access django admin: https:<DOMAIN>/admin
- Access django shell: exec -it <id of django-calendar-app> /app/manage.py shell_plus

## TODO
- [v] Add github action rebuilding image
- [v] Add DNS/SSL to the flow
- [ ] Add django superuser on the first deploy
