from subprocess import run
import sys

imagename = input("Enter image address: ")
run(["python", "detect.py", imagename])
run(["python", "spreadsheet.py", ])
run(["python", "identify.py", ])
