FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the service files
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "agent_app:app"]