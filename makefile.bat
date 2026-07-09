pyinstaller --exclude-module=tkinter --exclude-module=math --exclude-module=cmath --exclude-module=datetime --exclude-module=sys --exclude-module=os --exclude-module=cmd --exclude-module=subprocess --exclude-module=turtle --exclude-module=abc --exclude-module=decimal --exclude-module=importlib --exclude-module=io --exclude-module=traceback -F -n pypp pypp.py
move dist\pypp.exe .
del pypp.spec /q
del dist\ /q
del build\* /q
del build\ /q
pause