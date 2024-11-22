# Step 1: Use an official Python runtime as a base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app/

# Step 4: Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install django-material-admin

# Step 5: Expose the port that Django will run on
EXPOSE 8000

# Step 6: Set environment variables to use production settings
ENV PYTHONUNBUFFERED=1

# Step 7: Collect static files (optional for production)
# RUN python manage.py collectstatic --noinput

# Step 8: Command to run the Django development server (use Gunicorn for production)
CMD ["python", "manage.py","migrate",  "runserver", "0.0.0.0:8000"]
