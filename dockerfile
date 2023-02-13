FROM python:3

WORKDIR /schulklos

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_APP=schulkloskaputt.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
COPY . .

CMD [ "flask", "run" ]
