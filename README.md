# free_stacheltier
This tool has been created to factory reset IGEL thin clients.
Tested with firmware version 4 and 5.

## Motivation
If you are a proud owner of a IGEL thin client terminal which has been bought trough second hand you would like to reset it.
This requires to generate a challange (terminal key) which must be send to IGEL support.
IT people often work after sunset during hours without the IGEL service being reachable.
That frustrated me especially because I did want to reset more than one device. 

## Requirements
* linux system
* installed pycrypto package
* python2.7

## How to install

Install pycrypto and clone the git repo:
```
~ # pip install pycrypto
~ # git clone https://github.com/thomasDOTwtf/free_stacheltier.git
```
## How to use

Boot the your IGEL thin client and press ESC multiple times after the initial beep.
You'll see the following Menu. 
Choose "Factory Reset"

![Boot Menu](/img/reset_1.png)

The device will now prompt for admin credentials which you won't be able to provide.
Just enter an empty password three times. 
Enter "c" when prompted to reset.

![Boot Menu](/img/reset_2.png)

Your terminal key will now be displayed (marked red).
This key is needed to generate the factory reset key.

![Boot Menu](/img/reset_3.png)

Start free_stacheltier.py and enter your "terminal key":

```
~ # cd free_stacheltier/
~/free_stacheltier # python free_stacheltier.py
welcome to free_stacheltier.py
enter your igel terminal key below.
just press enter to exit

terminal key:63977-65351-11385-63785
Congratulations!
your reset key:
1549-33765-24557-48573
```

The generated reset key needed is:
**1549-33765-24557-48573**

Enter the key in the next dialog after entering "c"
  
![Boot Menu](/img/reset_4.png)

You will now be able to factory reset the device.
Just enter "yes" when prompted.
