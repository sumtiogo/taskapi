FROM python:3.9-alpine

WORKDIR /taskapi

ADD  requirements.txt .
RUN pip install -r requirements.txt

ADD taskapi/ ./taskapi

RUN flask --app taskapi init-db

EXPOSE 5000
CMD [ "flask", "--app", "taskapi", "run", "--host=0.0.0.0", "--port=5050" ]