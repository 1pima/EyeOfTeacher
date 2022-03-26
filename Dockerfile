FROM python:3.8

RUN mkdir -p /EyeOfTeacher

WORKDIR /EyeOfTeacher/

COPY Pipfile .
COPY Pipfile.lock .

RUN python3 -m pip install pipenv && pipenv install

RUN pipenv install

ENTRYPOINT ["pipenv", "run"]
