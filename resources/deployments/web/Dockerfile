FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install dependencies
RUN apk add --no-cache bash postgresql-client

# create non-root user and set media folder permissions
RUN addgroup -S app && adduser -S app -G app \
    && mkdir -p /app/resources/media \
    && chown -R app:app /app/resources/media

# switch to non-root user
USER app

WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Copy entrypoint script and make it executable
COPY resources/deployments/web/entrypoint /app/resources/deployments/web/entrypoint
RUN chmod +x /app/resources/deployments/web/entrypoint

ENTRYPOINT ["/app/resources/deployments/web/entrypoint"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers", "4", "config.wsgi:application"]
