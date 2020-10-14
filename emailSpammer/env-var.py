# Go to .bashrc / .bash-profile
# export PASS="your_password" 

import os 

password = os.environ.get('PASS')
print(password) 
