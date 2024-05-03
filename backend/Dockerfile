FROM python:3.10-slim

WORKDIR /cinema/backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD fastapi run main.py --port $PORT 