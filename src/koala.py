#!/usr/bin/env python
# sudo apt-get install python-configobj OR 
# easy_install configobj

try:
	import subprocess
	import os
	import sys
	from configobj import ConfigObj
	from optparse import OptionParser
	from PyQt4 import QtGui, QtCore

except ImportError as e:
	print "You do not have all the dependencies:"
	print str(e)
	sys.exit(1)
except Exception as e:
	print "An error occured when initialising one of the dependencies!"
	print str(e)
	sys.exit(1)

__author__ = "Dennis Schwertel"
__copyright__ = "Copyright (C) 2011 Dennis Schwertel"

options = []
CONFIGDIR = '../config'

def process():
	configs = os.listdir(CONFIGDIR)
	for chapter in configs:
		config = ConfigObj(os.path.join(CONFIGDIR, chapter))
		for group in config:
			for element in config[group]:
				cmd = []
				cmd.append("kwriteconfig")
				cmd.append("--file")
				cmd.append(chapter)
				cmd.append("--group")
				cmd.append(group)
				cmd.append("--key")
				cmd.append(element)
				cmd.append(config[group][element])
				if options.verbose:
					print ' '.join(cmd)
				if not options.dry:
					p = subprocess.call(cmd)

class RunButton(QtGui.QWidget):
	def run(self):
		process()
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Koala Configuration Setter')
		quit = QtGui.QPushButton('Set the Koala Configuration', self)
		quit.setGeometry(10, 10, 230, 130)
		self.connect(quit, QtCore.SIGNAL('clicked()'), self.run)


def main(argv):

	args = argv[1:]

	parser = OptionParser(usage = "just start me")
	parser.add_option("--dry", action="store_true", default=False, help="dry run")
	parser.add_option("--verbose", action="store_true", default=False, help="verbose")

	global options
	(options, args) = parser.parse_args(args)

	app = QtGui.QApplication(sys.argv)

	qb = RunButton()
	qb.show()
	#widget = QtGui.QWidget()
	#widget.resize(250, 150)
	#widget.setWindowTitle('simple')
	#widget.show()

	sys.exit(app.exec_())


if __name__ == '__main__':
	try:
		main(sys.argv)
	except Exception as e:
		print 'Unexpected error: ' + str(e)
		raise


