FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install .

EXPOSE 5000

CMD ["simple-flask-app"]
