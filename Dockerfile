# Use a highly secure, lightweight Linux/Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy ONLY the requirements first (this optimizes Docker's caching system)
COPY requirements.txt .

# Install dependencies securely without saving cache files
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set the tool to run as an executable CLI
ENTRYPOINT ["python", "main.py"]