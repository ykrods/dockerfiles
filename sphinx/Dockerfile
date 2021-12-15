FROM python:3.10

RUN pip install -U pip setuptools wheel

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Install direct dependencies. This is used when upgrading packages.
#
# docutils: https://github.com/sphinx-doc/sphinx/issues/9001
# RUN pip install sphinx docutils\<0.17 sphinx-autobuild sphinxcontrib-jsmath sphinxcontrib-mermaid sphinx-rtd-theme

CMD ["sphinx-build"]
