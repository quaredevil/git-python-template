#docker build -t quaredevil/test-ci:r12 . --no-cache
#docker push quaredevil/sync-gift:r0
#docker run --rm quaredevil/test-ci:r12
#====================================================#

FROM python:3.8-slim as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
# tracebacks explicitly, on a fault, after a timeout, or on a user signal
ENV PYTHONFAULTHANDLER=1
#
ENV PYTHONHASHSEED=random

ENV DEBIAN_FRONTEND=noninteractive

## Update
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        #build-essential \
        gcc libffi-dev g++ && \
    rm -rf /var/lib/apt/lists/*

# Sets utf-8 encoding for Python et al
ENV LANG=C.UTF-8

# Ensures that the python and pip executables used
# in the image will be those from our virtualenv.
ENV PATH="/venv/bin:$PATH"


WORKDIR /app

#====================================================#


FROM base as builder


ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1


RUN pip install "poetry"
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY . .

#Install
RUN . /venv/bin/activate && poetry install --no-interaction --no-ansi
#RUN . /venv/bin/activate && poetry install --no-root --no-interaction --no-ansi

#====================================================#

FROM base as final


COPY --from=builder /venv /venv
COPY --from=builder /app .
#COPY docker-entrypoint.sh ./


RUN . /venv/bin/activate && python3 simplecalc/cli.py sum 1 1
CMD ["sh", "-c", "tail -f /dev/null"]
#CMD ["./docker-entrypoint.sh"]
#====================================================#
