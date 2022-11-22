FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install netcat -y
RUN apt-get upgrade -y
RUN apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh .

COPY ./payment_service .

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000
