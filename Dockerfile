FROM python:3.9

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.1.8 \
    POETRY_HOME="/usr/local/py-utils" \
    POETRY_NO_INTERACTION=1 \
    PATH="/usr/local/py-utils/bin:$PATH" \
    PYTHONPATH="$PYTHONPATH:/app"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN poetry config virtualenvs.create false

EXPOSE 80

WORKDIR /app

COPY ./pyproject.toml ./
COPY ./poetry.lock ./
RUN poetry install --no-root

COPY ./app ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]