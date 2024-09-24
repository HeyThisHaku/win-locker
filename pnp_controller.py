from pnputil import get_devices,enable_devices,disable_devices
import keyboard



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
        keyboard.unblock_key(i)