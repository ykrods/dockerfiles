FROM python:3.12

RUN pip install -U pip setuptools wheel

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Install direct dependencies. This is used when upgrading packages.
#
# docutils: https://github.com/sphinx-doc/sphinx/issues/9001
RUN pip install sphinx sphinx-autobuild sphinxcontrib-jsmath sphinxcontrib-mermaid furo

CMD ["sphinx-build"]
