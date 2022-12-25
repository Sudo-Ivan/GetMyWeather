FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the files to the working directory
COPY . .

# Run the bot
CMD ["python3", "bot.py"]
