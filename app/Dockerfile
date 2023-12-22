FROM python:3.12

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"