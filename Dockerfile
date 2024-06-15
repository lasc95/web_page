FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "run.py"]
