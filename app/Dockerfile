FROM python:3.7-slim
WORKDIR /opt/nagp_app/
COPY src/requirements.txt .
RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt
COPY src/* .
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]