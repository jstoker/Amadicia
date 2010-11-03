#!/usr/bin/env python
import pygtk
pygtk.require('2.0')

import sys, random
import gtk
import gnomeapplet
import gobject

cycletime  = 1000 # 1 second
cycletime *= 60   # 1 min
cycletime *= 60   # 1 hour

label = None

def loadnames():
	f=None
	try:
		f=open('names.txt','r')
		text=f.read()
	finally:
		if f != None:
			f.close()
	return text.split('\n')

names = loadnames()

def name_change(applet):
	global label
	label.set_text(random.choice(names))
	gobject.timeout_add(cycletime, name_change, applet)

def amadicia_factory(applet, iid):
	global label
	label = gtk.Label("Generating...")
	applet.add(label)
	applet.show_all()

	name_change(applet)
	return True

if __name__ == '__main__':
	gnomeapplet.bonobo_factory("OAFIID:Amadicia_Factory", 
		gnomeapplet.Applet.__gtype__, 
		"Amadicia", "0.0.0", amadicia_factory)
