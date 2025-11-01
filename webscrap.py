


import pyfiglet 
print (pyfiglet.figlet_format('WEBSCRAP'))


import requests


url = input('ENTER YOUR SITE: ')

responcse = requests.get(url)

if responcse.status_code == 200 :
    print('Informaion get: ')
    print(responcse.json())
    
else :
    print('ERROR')    

