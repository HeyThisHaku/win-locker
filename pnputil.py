from winapi.cfgmgr32.constants import CM_GETIDLIST_FILTER_CLASS, CM_GETIDLIST_FILTER_NONE, CM_GETIDLIST_FILTER_PRESENT
from winapi.cfgmgr32.helper import get_device_via_instance_id, all_devices
from winapi.guid import GUID
from os import system

def disable_devices(instance_id:str):
    return system("pnputil /disable-device \"{}\" > %temp%/locker".format(instance_id))

def enable_devices(instance_id:str):
    return system("pnputil /enable-device \"{}\" > %temp%/unlocker".format(instance_id))

def get_devices(connected=True, instance_id: str = None, class_guid: str = None, class_name: str = None):
    if instance_id:
        def data_set(): return [get_device_via_instance_id(instance_id)] # Find devices based instancesIds
    else:
        flags = CM_GETIDLIST_FILTER_NONE
        filter_keyword = None

        if class_guid:
            GUID.is_valid(class_guid)
            filter_keyword = class_guid
            flags = CM_GETIDLIST_FILTER_CLASS

        if connected:
            flags = CM_GETIDLIST_FILTER_PRESENT
            
        def data_set(): return all_devices(filter_keyword=filter_keyword, flags=flags)
        
    list_devices = []
    for d in data_set():
        if(class_name):
            if(class_name.lower() == str(d.class_name).lower()):
                list_devices.append(d)
    return list_devices


if __name__=="__main__":
    print("Python implementation of Microsoft PnP Utility for enumeration only. Library only (This has been tested to work with Windows 10 and Python 3.9 64bit)")

# list_devices = get_devices(class_name="Mouse") 
# Propperty in devices:
# object.instance_id
# object.friendly_name or object.name  or object.desc 
# object.class_guid
# object.manufacturer
# object.driver_inf_path
# object.status
# object.class_name

