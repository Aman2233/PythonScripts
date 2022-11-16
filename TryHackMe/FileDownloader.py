import requests

url = 'https://assets.tryhackme.com/img/THMlogo.png' #Url link of the file
r = requests.get(url, allow_redirects=True) #request to get file while allowing redirects 
open('THMlogo.png', 'wb').write(r.content) #open the file 




#this is the  skeleton part of the programme 

#import  requests

#url = https://
#r = requests.get(url, allow_redirects= True)
#open('Name of file with extensiton', 'wb').write(r.content)
