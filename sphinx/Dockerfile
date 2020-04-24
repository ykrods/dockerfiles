FROM python:3.8.1

RUN pip install -U pip setuptools wheel && \
  pip install sphinx sphinx-autobuild sphinxcontrib-jsmath sphinxcontrib-mermaid sphinx_rtd_theme

CMD ["sphinx-build"]
