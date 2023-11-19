FROM python:3.10

WORKDIR /app

RUN apt upgrade

COPY requirements.txt main.py ./

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
