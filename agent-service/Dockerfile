# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

#Copy everything (including agent_app.py)
COPY . .

#Install dependencies after copying requirements.txt
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

#Run app using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "agent_app:app"]
