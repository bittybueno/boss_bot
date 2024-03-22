FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python application code into the container
COPY . .

# Command to run the Python application
CMD ["python", "src/boss_bot.py"]