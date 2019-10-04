# Just pass the command Line arguments as the location you want to view in google maps
# eg $ python3.py Lodhi Colony New Delhi 


import webbrowser, sys, pyperclip
any = sys.argv # the sys.argv returns the the command line argument as a list --> ['scrap.py', '2031', 'Delhi', 'Colony']

#check if command line arg is passed

if len(any) > 1:
	address = ' '.join(any[1:]) #To slice the list and take input from index 1
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+ address)

