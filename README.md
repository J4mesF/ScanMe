# ScanMe
Scan URL ,File by using virustotal API

<p align="center">
<img width="80" src="https://github.com/J4mesF/ScanMe/blob/master/img/me.jpg" /><br>
Scan With MEEEEEEE
</p>

## Table Of Contents
- [Install](#install)
- [Usage](#usage)
- [Note](#note)

## ScreenShot
<img src="https://raw.githubusercontent.com/J4mesF/ScanMe/master/img/1.png" /><br>
<img src="https://raw.githubusercontent.com/J4mesF/ScanMe/master/img/3.png" /><br>
<img src="https://raw.githubusercontent.com/J4mesF/ScanMe/master/img/2.png" /><br>
<br>

## Install
## Linux user
(python3).
You can install it by :
```bash
$ git clone https://github.com/J4mesF/ScanMe.git
$ cd  ScanMe
$ pip3 install -r requirements.txt 
```
## Window user
Download and extract the source [here](https://github.com/J4mesF/ScanMe)
Make sure you have already install python and pip3.
if you dont, get it [here](https://www.python.org/)
Open your window cmd and type:
```
C:\Users\Mrhope>pip3 install pyqt5
C:\Users\Mrhope>pip3 install requests
```
or:
```
C:\Users\Mrhope>pip3 install --user pyqt5
C:\Users\Mrhope>pip3 install --user requests
```
if its got error. You have to check is that you already install pip yet. Open cmd and type:
```
C:\Users\Mrhope>pip --version
```
if not you have to install it.Checkt it [here](https://www.liquidweb.com/kb/install-pip-windows/)

## Usage
To use this Tool you'll need a [Virustotal](https://www.virustotal.com/gui/home) API_KEY.
Go to the Virustotal [login](https://www.virustotal.com/gui/sign-in) page. 
Sign in.
Take your API_KEY 
And paste it [here](https://github.com/J4mesF/ScanMe/blob/master/ScanProcess/API_KEY/API_KEY.txt).  ScanMe/ScanProcess/API_KEY/API_KEY.txt 
If you don't have an account, You can get one [here](https://www.virustotal.com/gui/join-us)
Make sure that after [sign up](https://www.virustotal.com/gui/join-us) You have to cofirm your mail to active your account.

NOW YOU ARE GOOD TO GO!.
## LinuxUser
Just by this command:
```bash
$ python3 Run.py
```
## Window user
```
C:\Users\Mrhope>cd [PATH_TO_FILE]
C:\Users\Mrhope>python Run.py
```
## Note
Im still dealing with File Scan. It still have some bugs.
And just with File under 32MB.
There a guy had a good move on this API, you can check it out [here](https://github.com/tr4cefl0w/virustotal3).
See more about how to dealing with Virustotal API [here](https://developers.virustotal.com/v3.0/reference).

