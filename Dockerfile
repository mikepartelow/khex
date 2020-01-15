FROM python:3

RUN pip install pytz

COPY app /app

ENTRYPOINT /app/parse.py