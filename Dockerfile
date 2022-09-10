FROM python:3.9-alpine

ADD  requirements.txt .
RUN pip install -r requirements.txt

ADD main.py .

EXPOSE 5000
CMD [ "flask", "--app", "main", "run", "--host=0.0.0.0", "--port=5050" ]