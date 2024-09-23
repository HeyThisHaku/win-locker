@echo off
pyinstaller unlocker.py --onefile --distpath ./build --target-architecture x64
pyinstaller locker.py --onefile --distpath ./build --target-architecture x64 --add-data "lock.jpg;."