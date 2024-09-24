@echo off
pyinstaller  --onefile --distpath ./build --target-architecture x64 unlocker.py
pyinstaller --onefile --distpath ./build --target-architecture x64 locker.py 