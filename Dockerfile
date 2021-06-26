FROM python:3.9-alpine
WORKDIR /apps
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python", "./app.py" ]