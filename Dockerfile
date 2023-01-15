FROM python:3.10

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3

ENV PATH="/opt/poetry/bin:$PATH"

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/

COPY . /app

RUN poetry install --no-dev

RUN poetry run pytest

CMD ["poetry", "run", "uvicorn", "src.main:app",  "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info", "--forwarded-allow-ips", "*"]
