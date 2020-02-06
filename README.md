# FireTV_Remote
Control your FireTV with a simple python script and adb (Android Debug Bridge)


# 1
Enable ADB-Debugging. Go to the home tab on your FireTV Stick -> "Settings" -> "My Fire TV" -> "Developer options" -> set "ADB Debugging" to "ON"

# 2
Make sure adb is installed on your device. Otherwise install it via: https://www.xda-developers.com/install-adb-windows-macos-linux/

# 3
Get the IP-address of your FireTV-Stick. Append it with port 5555 so it will look something like: <your_ip>:5555 (e.g. 192.168.2.104:5555)

# 4
Clone this project and enter your FireTV's id in the FireTVController Class as the 'address' variable in "firetv_control.py". 

#5
Find the location of the installed adb executable and add the path in the FireTVController Class as the 'adb_path' variable in "firetv_control.py". 

#6 
Run 'firetv_control.py' with python3. You can use the following arguments to navigate with the script: 
- 'center' -> Center Button Press
- 'back' -> Back Button Press
- 'play' or 'pause' -> Play/Pause Button Press
- 'up', 'down', 'left', 'right' -> Navigation directions
- 'disconnect' -> Disconnect from adb

-- e.g. 'python3 firetv_control.py back left left center right disconnect'
