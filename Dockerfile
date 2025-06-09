FROM python:3.9-slim

# Prevent .pyc files and enable unbuffered output for logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user 'appuser' for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set working directory inside container
WORKDIR /app

# Install system dependencies needed for Pillow and PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Upgrade pip and install dependencies without cache to reduce image size
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Collect static files without prompt
RUN python manage.py collectstatic --noinput

# Expose port 8000 for the app
EXPOSE 8000

# Use Gunicorn with 3 workers for better concurrency
CMD ["gunicorn", "eshopper.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
