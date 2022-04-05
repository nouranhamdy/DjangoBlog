
FROM python:3.8

RUN mkdir -p /code

COPY . /code

WORKDIR /code

RUN pip install --no-cache-dir -r ./requirements.txt


CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
