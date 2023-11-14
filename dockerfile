FROM python:3.11-slim-bullseye

RUN pip install pytest requests selenium

WORKDIR /tests

# stands for 
# COPY EVERYTHING from LOCALFOLDER to CURRENT FODLER IN CONTAINER(which is /tests)
COPY . .

# specidfy command to run
CMD [ "pytest"]