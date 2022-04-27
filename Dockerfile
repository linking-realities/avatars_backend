# docker build -t django_test .
# docker run -p 8000:8000 django_test

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]