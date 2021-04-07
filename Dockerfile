FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
COPY ./src /app
RUN python -m pip install -r /app/requirements.txt