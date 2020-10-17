import psycopg2
from psycopg2 import connect
import os
import subprocess
import pytest

#def test_add():
#    true = 'true'
#    assert true

def check_conn(server):
    try:
        cmd = ('./nc.sh ' + server)
        lastline = os.popen(cmd).readlines()
        if 'succeeded' in str(lastline):
            psycopg2.connect("dbname='athena' user='athena'  host={}  password='welcomea' options='-c statement_timeout=1'".format(server))
            print("{} is reachable".format(server))
            return "success"
        else:
            print("{} is not reachable".format(server))
            return "fail"
    except:
        exit(1)
        return "fail"
def get_ip():
    try:
        cmd = 'kubectl get pod --context=kind-kind -o wide -n infra-system | awk {\'print $6\'} | tail -n 2'
        iplist = os.popen(cmd).readlines()
        return iplist
    except:
        exit(1)
#serverip = get_ip()
def test_pg_connect():
    serverip = get_ip()
    for l in serverip:
        conn_result = check_conn(l)
        print(conn_result)
        assert conn_result == "success"
