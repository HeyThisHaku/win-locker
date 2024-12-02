from pnputil import get_devices,enable_devices,disable_devices
import keyboard
import os
import signal

PID_NAME = "lock.pid"
TEMP_PATH = os.getenv("TEMP", "")

def read_pid_file():
    pid_file_path = os.path.join(TEMP_PATH, PID_NAME) 
    if not os.path.isfile(pid_file_path):
        raise FileNotFoundError(f"The file {pid_file_path} does not exist.")
    
    with open(pid_file_path, "r") as file:
        content = file.read()
    
    return content

def delete_pid_file():
    if not TEMP_PATH:
        raise EnvironmentError("TEMP path is not set.")
    
    pid_file_path = os.path.join(TEMP_PATH, "lock.pid")
    
    if os.path.isfile(pid_file_path):
        os.remove(pid_file_path) 
        print(f"File {pid_file_path} has been deleted.")
    else:
        raise FileNotFoundError(f"The file {pid_file_path} does not exist.")

def lock_mouse():
    get_mouses = get_devices(class_name="Mouse")
    for d in get_mouses:
        disable_devices(str(d.instance_id))

def unlock_mouse():
    get_mouses = get_devices(class_name="Mouse")
    for d in get_mouses:
        enable_devices(str(d.instance_id))

def lock_keyboard():
    for i in range(150):
        keyboard.block_key(i)

def unlock_keyboard():
    for i in range(150):
        try:
            keyboard.unblock_key(i)
        except:
            pass
    # Kill LAST CMD
    os.kill(int(read_pid_file()), signal.SIGTERM)
    delete_pid_file()