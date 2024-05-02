FROM python:3.11


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


copy requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python0", "manage.py", "runserver", "0.0.0.0:80"]