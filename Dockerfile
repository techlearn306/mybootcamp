
FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE  9090
ENV FLASK_APP=app.py
CMD ["flask", "run","--port","9090","--host", "0.0.0.0"]
