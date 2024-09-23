from pnputil import get_devices,enable_devices,disable_devices

def lock_mouse():
    get_mouses = get_devices(class_name="Mouse")
    for d in get_mouses:
        disable_devices(str(d.instance_id))

def unlock_mouse():
    get_mouses = get_devices(class_name="Mouse")
    for d in get_mouses:
        enable_devices(str(d.instance_id))

def lock_keyboard():
    get_keyboards = get_devices(class_name="Keyboard")
    for d in get_keyboards:
        disable_devices(str(d.instance_id))

def unlock_keyboard():
    get_keyboards = get_devices(class_name="Keyboard")
    for d in get_keyboards:
        enable_devices(str(d.instance_id))