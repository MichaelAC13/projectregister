# DOCUMENTATION

Test with postman doc:
https://documenter.getpostman.com/view/18943270/UzQyq3ph

# TO RUN IN LOCAL EDITOR - WINDOWS
Requirements:
pip install requirements.txt
if running with code editor, remember to run also with python 'env'

# FLASK BASIC STRUCT FOR HEROKU

python-3.8.6

In the project directory, you can run:

```bash
    python -m venv env
```

For activate script:

```bash
    ./env/Scripts/actaivte
```
Runs the app in the development mode.\

```bash
    python app.py
```
# TO RUN IN DOCKER IMAGE

Requirements:
FROM python:3
COPY . /app
RUN pip install flask && pip install flask-cors && pip install pyjwt && pip install pymongo
WORKDIR /app
CMD python app.py

# Have fun!
