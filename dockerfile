FROM python:3.11-slim-bullseye

RUN pip install pytest requests selenium faker pytest-html

WORKDIR /tests

# stands for 
# COPY EVERYTHING from LOCALFOLDER to CURRENT FODLER IN CONTAINER(which is /tests)
COPY . .

ENTRYPOINT ["pytest" ]
# specidfy command to run
CMD ["--html=reports/report.html", "--self-contained-html"] 