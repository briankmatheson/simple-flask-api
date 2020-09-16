FROM python:3.7.2-stretch

WORKDIR /api
COPY api/requirements.txt /api

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

COPY api /api
ENTRYPOINT ["/api/run.sh"]
