#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd
from websocket import create_connection

class Cli(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "> "
		self.intro = "Доброго временисуток"
		self.doc_header = "HELP"

	def do_test(self, args):
		N = int(input('Введите кол-во подключений: '))
		M = int(input('Введите кол-во запросов: '))

		for i in range (N):
		    ws = create_connection ("ws://localhost/echo")
		    print str(i)
		    for y in range(M):
		        ws.send('Hello, World'+str(y))
		        result = ws.recv()
		        print result
		        ws.close
		print "help world"

	def default(self, line):
		print "Error"

if __name__ == "__main__":
	cli = Cli()
	try:
		cli.cmdloop()
	except KeyboardInterrupt:
		print "bye bye"
