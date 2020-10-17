FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python3-pytest-cov
RUN apt-get install -y curl
RUN apt-get install -y libpq-dev
RUN apt-get install -y python3-pip
RUN pip3 install psycopg2
COPY --from=lachlanevenson/k8s-kubectl:v1.18.1 /usr/local/bin/kubectl /usr/local/bin/kubectl
COPY check_pg.py .
COPY nc.sh .

CMD "pytest-3 test_check_pg.py -s"
CMD "while true; do python3 check_pg.py && echo 'OK' || echo 'FAIL'; sleep 1; done > /tmp/1.txt"

