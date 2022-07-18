FROM python:3
COPY . /app
RUN pip install flask && pip install flask-cors && pip install pyjwt && pip install pymongo
WORKDIR /app
CMD python app.py