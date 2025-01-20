# Use the official Python slim image
FROM python:3.9-slim-buster

# Install necessary system dependencies including awscli and pip tools
RUN apt update -y && \
    apt install -y awscli && \
    apt install -y --no-install-recommends gcc libc-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the project files
COPY . /app

# Upgrade pip and install requirements with a higher timeout and retries
RUN python3 -m pip install --upgrade pip setuptools wheel && \
    pip install --timeout=300 --retries=5 --index-url https://pypi.org/simple -r requirements.txt

# Define the command to run the application
CMD ["python3", "app.py"]
