# AutoPart

### Set environment variables

```sh
cp .env.example .env
```

### Build docker

```sh
docker-compose build
```

### Run python migrations

```sh
docker-compose run server python manage.py migrate
```

### Create superuser

```sh
docker-compose run server python manage.py createsuperuser
```

### Run docker

```sh
docker-compose up
```
