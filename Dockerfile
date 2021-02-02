FROM continuumio/miniconda3:4.9.2-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN /opt/conda/bin/conda install -y django mysqlclient gunicorn Pillow
RUN /opt/conda/bin/pip install -r /requirements.txt
RUN mkdir /app
# COPY ./src /app
WORKDIR  /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
CMD ["entrypoint.sh"]
