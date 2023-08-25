FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m unittest test.py

EXPOSE 5000

CMD ["python", "app.py"]
