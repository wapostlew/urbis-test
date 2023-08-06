FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /server

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt -o requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh /server/
COPY ./app /server/app

RUN chmod +x /server/start.sh
CMD ["/server/start.sh"]