import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_Pat = "C:/Users/gargi/OneDrive/Desktop/fir"
dst_pat = "C:/Users/gargi/Downloads/dst_Path"

ex = {
    "Images": [".png",".jpg"],
    "Models 3D": [".fbx",".obj"],
    "Zip": [".zip"],
    "Pdf": {".pdf"}
}

class FileMove(FileSystemEventHandler):
    def on_created(self, event):
        print(f"something is new made in {event.src_path}")

    def on_deleted(self, event):
        print(f"something is deleted in {event.src_path}")

    def on_modified(self, event):
        print(f"modified{event.src_path}")

    def on_moved(self, event):
        print(f"it is moved{event.src_path},{event.dest_path}")

event_handler = FileMove()

observer = Observer()

observer.schedule(event_handler,src_Pat, recursive=True)

observer.start()

try:
   while True:
       time.sleep(1)
       print("run")
except KeyboardInterrupt:
    observer.stop()