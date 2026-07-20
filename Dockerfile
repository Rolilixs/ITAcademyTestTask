ARG PYTHON_VERSION=3.13.1
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "backend.main:app", "--host", "localhost", "--port", "8000"]