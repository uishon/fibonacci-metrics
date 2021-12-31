FROM python:3.9-slim-buster
WORKDIR  /opt/fibonacci
COPY fibonacci-calculator-with-metrics.py requirements.txt ./
RUN pip install -r requirements.txt
CMD [ "python3", "./fibonacci-calculator-with-metrics.py" ] 