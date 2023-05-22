FROM python:3

WORKDIR /schulklos

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=schulkloskaputt.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY app/static app/static
COPY app/templates app/templates
COPY app/__init__.py app/__init__.py
COPY app/config.py app/config.py
COPY app/forms.py app/forms.py
COPY app/models.py app/models.py
COPY app/routes.py app/routes.py

COPY .flaskenv .flaskenv
COPY README.md README.md
COPY schulkloskaputt.py schulkloskaputt.py

RUN flask db init
RUN flask db migrate -m "initial"
RUN flask db upgrade

CMD [ "flask", "run" ]
