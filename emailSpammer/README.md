# Script used for sending emails
## Usage 
#### Update the code with your credentials and run ####
``` python3 spam.py ```
###### This is just a demo of how email can be sent through the script you can modify it according to your needs for eg Spamming someone by putting the code in a for loop, sending different messages to different address etc


#### Adding environment variables to your OS
1. Go to: `.bashrc` for ubuntu and `.bash-profile` in MacOS
2. Type `export PASS="your_secret_password"`
3. Acess it anywhere in your system as:
```
import os
password = os.environ.get('PASS')
```