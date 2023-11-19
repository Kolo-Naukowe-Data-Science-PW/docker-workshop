# Using ready ubuntu images from dockerhub

Check out: https://hub.docker.com/

### Pull ubuntu image

```bash
docker pull ubuntu:latest
```

### Run ubuntu container

```bash
docker run ubuntu:latest
```

### Run ubuntu container interactively (-i) with tty (-t) so it doesn't stop and name it (--name)

```bash
docker run --name myubuntu -it ubuntu:latest
```

### Execute a command inside that conatiner using a different bash 

```bash
docker exec myubuntu touch /home/aaa
```

### Stop and restart the container

```bash
docker stop myubuntu
docker start myubuntu
docker exec -it myubuntu bash
```

