import os, platform, json, time
import psutil



def get_system_info():


    # Get system information
    system_info = {}
    system_info['system'] = platform.system()
    system_info['node'] = platform.node()
    system_info['release'] = platform.release()
    system_info['version'] = platform.version()
    system_info['processor'] = platform.machine()


    # Return system information as JSON
    return json.dumps(system_info)
