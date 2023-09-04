# fetch-receipt-processor
Backend coding challenge for Fetch

## Ways to launch backend
Before accessing the server, do not forget to replace the DJANGO_SECRET_KEY value in django.env!
### 1. Docker
Enter receipt_processor project (where Dockerfile is)
```
cd receipt_processor
```
Build the Docker Image
```
docker build -t receipt_processor .
```
Run the Docker Container
```
docker run -d -p 8000:8000 receipt_processor
```
Access the server at https://localhost:8000
### 2. Locally
This project uses pipenv as a python package manager. Essentially, it's pip and venv combined, once you're in pipenv's virtual environment, just treat pipenv as you would pip commands. For more information see here: https://realpython.com/pipenv-guide/

Install pipenv (or with homebrew for mac)
```
pip install pipenv
```
Enter receipt_processor project (where Pipfile is)
```
cd receipt_processor
```
Create and enter pipenv virtual environment
```
pipenv shell
```
Install Pipfile.lock
```
pipenv install
```
Start django (https://localhost:8000)
```
python manage.py runserver
```
Exit virtual environment
```
exit
```
