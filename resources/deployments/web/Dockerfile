FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies
RUN apk add --no-cache bash postgresql-client

# Copy requirements and install Python packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Copy entrypoint script and make it executable
COPY resources/deployments/web/entrypoint /app/resources/deployments/web/entrypoint
RUN chmod +x /app/resources/deployments/web/entrypoint

# Set entrypoint and default command
ENTRYPOINT ["/app/resources/deployments/web/entrypoint"]
CMD ["gunicorn", "-b", "0.0.0.0:8069", "--workers", "4", "config.wsgi:application"]
