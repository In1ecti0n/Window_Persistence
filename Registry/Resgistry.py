import os
import ctypes
from ctypes import windll
from ctypes import wintypes
#https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-functions
advapi32 = windll.LoadLibrary('Advapi32.dll')

#https://github.com/python/cpython/blob/main/Lib/ctypes/wintypes.py
RegCreateKey = advapi32.RegCreateKeyExW
RegCreateKey.argtypes = [wintypes.HKEY, wintypes.LPCWSTR, wintypes.DWORD, wintypes.LPWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.PHANDLE,wintypes.LPDWORD]

RegSetValue = advapi32.RegSetValueExW
RegSetValue.argtypes = [wintypes.HKEY,wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,wintypes.LPCWSTR,wintypes.DWORD]

RegCloseKey = advapi32.RegCloseKey
RegCloseKey.argtypes = [wintypes.HKEY]

RegDeleteKey = advapi32.RegDeleteKeyExW
RegDeleteKey.argtypes = [wintypes.HKEY, wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD]

RegOpenKey = advapi32.RegOpenKeyExW
RegOpenKey.argtypes = [wintypes.HKEY,wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,ctypes.POINTER(wintypes.HKEY)]

RegDeleteValue = advapi32.RegDeleteValueW
RegDeleteValue.argtypes = [wintypes.HKEY,wintypes.LPCWSTR]

def create_new_key(Hkey, subkey):
    handle = wintypes.HKEY()
    RegCreateKey(Hkey, subkey, 0, None, 0x00000000, 0x20006, None, ctypes.byref(handle), None)
    RegCloseKey(handle)

def create_new_key_value(Hkey, subkey, valueName, valueData):
    handle = wintypes.HKEY()
    RegCreateKey(Hkey, subkey, 0, None, 0x00000000, 0x20006, None, ctypes.byref(handle), None)
    RegSetValue(handle, valueName, 0, 1, valueData, (len(valueData) + 1) * ctypes.sizeof(wintypes.WCHAR))
    RegCloseKey(handle)

def delete_key(Hkey, subkey):
    RegDeleteKey(Hkey, subkey, 0x0100, 0)

def delete_value(Hkey, subkey, valueName):
    handle = wintypes.HKEY()
    RegOpenKey(Hkey, subkey, 0, 0x20006, ctypes.byref(handle))
    RegDeleteValue(handle, valueName)
    RegCloseKey(handle)



while(1):
    print("1.Create new key")
    print("2.Create new key value")
    print("3.Delete key")
    print("4.Delete key value")
    index = input("Choose number option you want:")
    if index == '1':
        subkey = input("Your key name:")
        t = input("*HKEY_CURRENT_USER || **HKEY_LOCAL_MACHINE, which one:")
        if t == '*':
            create_new_key(0x80000001, subkey)
        else:
            create_new_key(0x80000002, subkey)
        break
    elif index == '2':
        subkey = input("Your key name:")
        valueName = input("Your value name:")
        valueData = input("Your value data:")
        t = input("*HKEY_CURRENT_USER || **HKEY_LOCAL_MACHINE, which one:")
        if t == '*':
            create_new_key_value(0x80000001, subkey, valueName, valueData)
        else:
            create_new_key_value(0x80000002, subkey, valueName, valueData)
        break
    elif index == '3':
        subkey = input("Your key name:")
        t = input("*HKEY_CURRENT_USER || **HKEY_LOCAL_MACHINE, which one:")
        if t == '*':
            delete_key(0x80000001, subkey)
        else:
            delete_key(0x80000002, subkey)
        break
    elif index == '4':
        subkey = input("Your key name:")
        valueName = input("Your value name:")
        t = input("*HKEY_CURRENT_USER || **HKEY_LOCAL_MACHINE, which one:")
        if t == '*':
            delete_value(0x80000001, subkey, valueName)
        else:
            delete_value(0x80000002, subkey, valueName)
        break
    else: 
        index = input("Retype number option you want:")
        
#HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
#HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run