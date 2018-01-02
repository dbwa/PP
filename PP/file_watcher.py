#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.DEBUG)
path="."  #working directory

class MyEventHandler(FileSystemEventHandler):
	def catch_all_handler(self, event):
		logging.debug(event)

	def on_moved(self, event):
		self.catch_all_handler(event)
		print("Warning : moving or renaming object inside the drop-zone can lead to errors. ")

	def on_created(self, event):
		self.catch_all_handler(event)
		print("hello")

	def on_deleted(self, event):
		self.catch_all_handler(event)
		print("byebye")

	def on_modified(self, event):
		self.catch_all_handler(event)
		print("Warning : moving or renaming object inside the drop-zone can lead to errors. ")

	def execute(self):
		
		pass  #là on mettra le truc a faire quand y'aura un nouveau fichier

event_handler = MyEventHandler()

observer = Observer()
observer.schedule(event_handler, path=path, recursive=False)
observer.start()
try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()
