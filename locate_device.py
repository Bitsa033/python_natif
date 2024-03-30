import socket                                                                 
import requests                                                                                 
# obtenir l'adresse à partir d'un nom de domaine (DNS)                                   
ip_address = socket.gethostbyname('pythoniaformation.com')                    
# print(ip_address)        
# recuperer les informations                            
response = requests.get(f'http://ip-api.com/json/{ip_address}')               
location_info = response.json()                                               
print(location_info)