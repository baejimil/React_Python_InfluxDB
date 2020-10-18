FROM python:3.8-slim

WORKDIR /app/api

COPY requirements.txt /app/api/requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]