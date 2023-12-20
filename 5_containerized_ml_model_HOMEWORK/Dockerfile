FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get upgrade

COPY requirements.txt model.pkl ./

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
