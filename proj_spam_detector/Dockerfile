# Set base python image
FROM python:3.8.3

# File author
MAINTAINER Rizwan

# Set base directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/requirements.txt

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Allow port 8000
EXPOSE 8000

# Command to start the web server
CMD exec gunicorn proj_spam_detector.wsgi:application --bind 0.0.0.0:8000 --workers 2
