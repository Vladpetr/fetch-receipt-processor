FROM python:3.10

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv

ARG DJANGO_SECRET_KEY
# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy --ignore-pipfile

# Copy the current directory contents into the container at /app/
COPY . /app/

EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]