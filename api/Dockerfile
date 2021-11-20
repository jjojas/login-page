# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# WORKDIR /fastapi
# COPY ./app /app
# COPY requirements.txt requirements.txt
# RUN python -m pip install -r requirements.txt
# EXPOSE 8000

FROM python:3.7
WORKDIR /fastapi
COPY ./app ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]