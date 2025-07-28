FROM python:3.11-slim-bullseye

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY . /app

RUN uv pip install --no-cache-dir --system -r requirements.txt

CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8082", "--log-level", "info", "--use-colors"]
