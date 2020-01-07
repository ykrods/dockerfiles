FROM python:3.8.1

# TODO: support plantUML
RUN apt-get update && \
  apt-get install -y openjdk-11-jre graphviz
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

CMD ["python", "/opt/sphinx-server/server.py"]
