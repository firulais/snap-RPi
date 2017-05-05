@echo off
setlocal ENABLEEXTENSIONS

@echo "seraching python in ..."
@echo PYTHONPATH = %PYTHONPATH%
IF EXIST %PYTHONPATH% set instpath=%PYTHONPATH%
IF EXIST C:\Python34\ set instpath=C:\Python34\
@echo LOCALAPPDATA = %LOCALAPPDATA%
IF EXIST %LOCALAPPDATA%\Programs\Python\Python35\ set instpath=%LOCALAPPDATA%\Programs\Python\Python35\
@echo PROGRAMFILES = %PROGRAMFILES%
IF EXIST %PROGRAMFILES%\Python 3.5\ set instpath=%PROGRAMFILES%\Python 3.5\
IF EXIST %PROGRAMFILES%\Python36\ set instpath=%PROGRAMFILES%\Python36\

@echo "searching in registry ..."
set KEY_NAME="HKLM\SOFTWARE\Wow6432Node\Python\PythonCore"
for /f "tokens=*" %%A in ('REG QUERY %KEY_NAME%^|find /i "PythonCore\3"') do SET "PYKEY=%%A"
set KEY_NAME=%PYKEY%\InstallPath
set KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Python\PythonCore\3.4\InstallPath"
for /f "tokens=3 skip=2" %%A in ('REG QUERY %KEY_NAME% /ve') do SET "instpath=%%A"

@echo instpath = %instpath%
IF EXIST %instpath% set PATH=%PATH%;%instpath%

python.exe -O RPiGPIO.py
pause