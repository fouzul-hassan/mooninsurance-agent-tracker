# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application code and dependencies
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Copy test files
# COPY templates ./templates
# COPY tests ./tests

# Expose the application port
EXPOSE 5000

# Run the flask application
CMD ["python", "integration_app.py"]