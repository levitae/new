FROM python:3.9-slim-buster
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
