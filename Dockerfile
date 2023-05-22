FROM python:latest

ENV CHOKIDAR_USEPOLLING 1

RUN apt-get update && apt-get install nodejs -y --no-install-recommends
RUN apt-get update && apt-get install npm -y --no-install-recommends

RUN pip install Flask
RUN pip install redis[hiredis]

WORKDIR /app
COPY nodemon.json /app/
VOLUME /app

RUN export FLASK_APP=app
RUN export FLASK_ENV=development

RUN npm i nodemon

EXPOSE 5000

CMD [ "npx", "nodemon", "--watch", "**/*", "--exec", "python3", "./app.py" ] 