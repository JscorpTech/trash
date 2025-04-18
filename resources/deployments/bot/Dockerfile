FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
RUN apk add --no-cache bash postgresql-client

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

COPY resources/deployments/bot/entrypoint /app/resources/deployments/bot/entrypoint
RUN chmod +x /app/resources/deployments/bot/entrypoint

ENTRYPOINT ["/app/resources/deployments/bot/entrypoint"]
CMD ["python", "run.py"]