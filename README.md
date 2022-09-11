
# For App User

## how to start this app

```shell
$ docker-compose up --build
```

tested docker version

```shell
$ docker --version
Docker version 20.10.17, build 100c701
$ docker-compose --version
Docker Compose version v2.10.2
```

# For App Developer

run following command and then happy developing
```shell
$ flask --app taskapi init-db
$ flask --app taskapi --debug run
```

## References

- [flask](https://flask.palletsprojects.com/en/2.2.x/)
- [docker compose](https://docs.docker.com/compose/)
- [github action](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)