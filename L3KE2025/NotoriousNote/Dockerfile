FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libappindicator1 \
    fonts-liberation \
    libnss3 \
    lsb-release \
    gnupg \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy app source code
COPY src/ /app
COPY requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=app.py

# Run the app
CMD ["flask", "run", "--host=0.0.0.0"]