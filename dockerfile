FROM python:3.13-slim

# Install system dependencies that many Python packages (e.g. psycopg2, Pillow) often need
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory *before* copying
WORKDIR /app

# Copy app code and requirements
COPY ./greyhoundDashboard/ /app/
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Expose Django development port (optional in production)
EXPOSE 8000

# Run the dev server (not recommended for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
