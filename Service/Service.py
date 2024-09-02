import os
import ctypes
from ctypes import wintypes
from ctypes import windll

# Cac hang so dinh nghia thuoc tinh dich vu https://learn.microsoft.com/en-us/windows/win32/services/service-functions ;  https://www.geoffchappell.com/studies/windows/win32/advapi32/api/index.htm


# Goi thu vien C Advapi32.dll
advapi32 = windll.LoadLibrary('Advapi32.dll')

# Dinh nghia kieu du lieu cho cac ham 
OpenSCManager = advapi32.OpenSCManagerW
OpenSCManager.artypes = [wintypes.LPWSTR,wintypes.LPWSTR,wintypes.DWORD]
OpenSCManager.restype = wintypes.HANDLE

OpenService = advapi32.OpenServiceW
OpenService.argtypes = [wintypes.HANDLE, wintypes.LPWSTR, wintypes.DWORD]
OpenService.restype = wintypes.HANDLE

CreateService = advapi32.CreateServiceW
CreateService.argtypes = [wintypes.HANDLE, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR]
CreateService.restype = wintypes.HANDLE

DeleteService = advapi32.DeleteService
DeleteService.argtypes = [wintypes.HANDLE]
DeleteService.restype = wintypes.BOOL

ChangeServiceConfig = advapi32.ChangeServiceConfigW
ChangeServiceConfig.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR, wintypes.LPWSTR]
ChangeServiceConfig.restype = wintypes.BOOL

CloseServiceHandle = advapi32.CloseServiceHandle
CloseServiceHandle.argtypes = [wintypes.HANDLE]
CloseServiceHandle.restype = wintypes.BOOL



# Bat dau chuong trinh
def create_service(serviceName, displayName, path):   #https://learn.microsoft.com/en-us/windows/win32/services/installing-a-service
    SCManager = OpenSCManager(None, None, 0x0002)
    NewService = CreateService(SCManager, serviceName, displayName, 0xF003F, 0x00000010, 0x00000002, 0x00000001, path, None, None, None, None, None)
    CloseServiceHandle(SCManager)
    CloseServiceHandle(NewService) 

def delete_service(serviceName):                      #https://learn.microsoft.com/en-us/windows/win32/services/deleting-a-service
    SCManager = OpenSCManager(None, None, 0x0002)
    Service = OpenService(SCManager, serviceName, 0x10000)
    DeleteService(Service)
    CloseServiceHandle(SCManager)
    CloseServiceHandle(Service) 

def change_service(serviceName, type):
    SCManager = OpenSCManager(None, None, 0x0002)
    Service = OpenService(SCManager, serviceName, 0xF003F)
    ChangeService = ChangeServiceConfig(Service, 0xFFFFFFFF, type, 0xFFFFFFFF, None, None, None, None, None, None)
    CloseServiceHandle(SCManager)
    CloseServiceHandle(ChangeService) 


while(1):
    print("1. Create Service:")
    print("2. Delete Service:")
    print("3. Change state of service:")
    index = input("Choose number option you want:")
    if index == '1':
        serviceName = input("Type your service name:")
        displayName = input("Type your service display:")
        path = input("Path:")
        create_service(serviceName, displayName, path)
        break
    elif index == '2':
        serviceName = input("Type your service name:")
        delete_service(serviceName)
        break
    elif index == '3':
        serviceName = input("Type your service name:")
        type = input("Type you want (Auto:0x00000002; Boot:0x00000000; Disable:0x00000004):") 
        change_service(serviceName, type)
        break
    else:
        index = input("Retype number option you want:")
