# Use an official Python image as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Create a non-root user to run the application
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Install system dependencies and apply security updates
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the files to the working directory
COPY . .

# Change the ownership of the app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Run the bot
CMD ["python3", "bot.py"]
