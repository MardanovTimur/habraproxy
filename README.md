# habraproxy
Proxy localhost server for habr users

Run proxy server (hot-reloading is enabled by default):
```bash
# Notice! activate yours virtual environment and install libraries
$ pip3 install -r requirements.txt
$ adev runserver app/main.py
```

Docker
```bash
$ docker build . --tag timur/habrproxy:latest
$ docker run -it -p 8000:8000 timur/habrproxy:latest
```
