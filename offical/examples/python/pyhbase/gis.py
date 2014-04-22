#!/usr/bin/env python
import sys

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

usage = """gis.py action ...
  help - print this messsage and exit
  list - list all installed users."""

class TwitBaseConn(object):
    def __init__(self, host="localhost", port=9090):
        transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)
        self.transport.open()

    def close(self):
        self.transport.close()

    def list_tables(self):
	return self.client.getTableNames()

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if len(args) == 0 or 'help' == args[0]:
        print usage
        raise SystemExit()

    twitBase = TwitBaseConn()

    if args[0] == 'list':
        for user in twitBase.list_tables():
            print user

    twitBase.close()

if __name__ == '__main__':
    main()
