# FROM python:3.8.5-alpine3.12

# WORKDIR /usr/src/app

# COPY . .
# RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "python", "app.py" ]


FROM python:3.8-slim-buster

WORKDIR /application
ADD . /application
COPY . .

RUN mkdir ~/.pip


RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

CMD ["python", "app.py"]


ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "application.wsgi:app", "--daemon", "--reload"]

