FROM python:3.6
MAINTAINER TimurMardanov, timurmardanov97@gmail.com

WORKDIR /usr/src/application

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8001

CMD [ "adev", "runserver", "app/main.py" ]
