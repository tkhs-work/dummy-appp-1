FROM python:3.6
  
#WORKDIR /app
#ADD . app

COPY src/app.py .
COPY src/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]