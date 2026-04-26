FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt .
RUN uv sync

COPY . .

EXPOSE 8000

CMD ["gunicorn", "run:app"]