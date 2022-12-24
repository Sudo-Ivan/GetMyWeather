FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the files to the working directory
COPY . .

# Run the bot
CMD ["python3", "bot.py"]
