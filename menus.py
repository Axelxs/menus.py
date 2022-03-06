import requests
import json
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email.mime.text import MIMEText
import socket
import telebot  
import logging
import asyncio
import sys
from time import sleep
from http.server import BaseHTTPRequestHandler
import time
import os
import platform
from datetime import datetime
import binascii
import ipaddress
import platform

RR = "\033[29;m"
def a(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./170)

a(RR+"╭━╮╭━╮╭━━━╮╭━╮╱╭╮╭╮╱╭╮   ╭━━━╮╭━━━╮╭━━━╮╭━━╮╭━━━╮╭━━━━╮╭━━━╮")
a(RR+"┃┃╰╯┃┃┃╭━━╯┃┃╰╮┃┃┃┃╱┃┃   ┃╭━╮┃┃╭━╮┃┃╭━╮┃╰┫┣╯┃╭━╮┃┃╭╮╭╮┃┃╭━╮┃")
a(RR+"┃╭╮╭╮┃┃╰━━╮┃╭╮╰╯┃┃┃╱┃┃   ┃╰━━╮┃┃╱╰╯┃╰━╯┃╱┃┃╱┃╰━╯┃╰╯┃┃╰╯┃╰━━╮")
a(RR+"┃┃┃┃┃┃┃╭━━╯┃┃╰╮┃┃┃┃╱┃┃   ╰━━╮┃┃┃╱╭╮┃╭╮╭╯╱┃┃╱┃╭━━╯╱╱┃┃╱╱╰━━╮┃")
a(RR+"┃┃┃┃┃┃┃╰━━╮┃┃╱┃┃┃┃╰━╯┃   ┃╰━╯┃┃╰━╯┃┃┃┃╰╮╭┫┣╮┃┃╱╱╱╱╱┃┃╱╱┃╰━╯┃")
a(RR+"╰╯╰╯╰╯╰━━━╯╰╯╱╰━╯╰━━━╯   ╰━━━╯╰━━━╯╰╯╰━╯╰━━╯╰╯╱╱╱╱╱╰╯╱╱╰━━━╯")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")

a(RR+" Creador: Axel")      
a(RR+" Tiktok: axel.is.pastriboy")
print("")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
choice = int(input("1.-BOTNET  TIKTOK\n2.-ESCANEO WEP\n3.-spam de correos gmail\n4.-info de IP publica\n5.-Servidor privado http\n6.-Mi IP privada \n7.-info basica de cualquier tipo de ip \n8.-Info de un numero\n9.-Barrido de IP\nSeleccione una opsion: ")) 
b = 1         
if choice == 1:
                    print("\033[;32m")
                    username = ""
                    username = input("usuario:")
                    while b < 9999999999999999999999:
                        print (("[*]"),"REPORT-BOT FOR TIKTOK USER @", (username), (b))
                        sleep(1)
                        b = b + 1
                    quit()
                
                  
                  
                  
elif choice == 2:
    a = ""
    a = input("ingresa el dominio wep:")
    TARGETS = [
    ((a), 'https')
    ]
    
    
    async def main(loop, targets):
            for target in targets:
                info = await loop.getaddrinfo(
                *target,
                proto=socket.IPPROTO_TCP,
            ) 
             
            for host in info:
                print('{:20}: {}'.format(target[0], host[4][0]))
        
    event_loop = asyncio.get_event_loop()
    try:
            event_loop.run_until_complete(main(event_loop, TARGETS))
    finally:
            event_loop.close()
    try:
            print("escaneo exitoso")
    except:
                print("ERROR")
                quit()
                  
elif choice == 3:
    print("\033[;32m")
    print ("SMPAM DE GMAIL")
    sleep(0.7)
    print ("cada atake trae 100 correos")
    sleep(0.7)
    gmail = ""
    gmail = input("Gmail de la bictima :")
    asunto = ""
    asunto = input("Asunto del correo:")
    texto = ""
    texto = input("texto del correo:")
    a = 0
    while a < 100:
        mensaje =  MIMEMultipart ()
        mensaje ["from"] = "gogle.spport.mx@gmail.com"
        mensaje ["To"] = (gmail)
        mensaje ["subject"] = (asunto)
        mensaje = MIMEText (texto)
        smtp = SMTP ("smtp.gmail.com")
        smtp.starttls()
        smtp.login("gogle.spport.mx@gmail.com", "gogle2000")
        smtp.sendmail ("gogle.spport.mx@gmail.com", (gmail), mensaje.as_string())
        smtp.quit()
    a = a +1
                      
                      
elif choice == 4:
  
  api_url = "http://ip-api.com/json/"
  parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
  data = {"fields":parametros}
  def ip_scraping(ip=""):
      res = requests.get(api_url+ip, data=data)
      api_json_res = json.loads(res.content)
      return api_json_res
  if __name__ == '__main__':
          ip = input("𝙄𝙉𝙂𝙍𝙀𝙎𝘼 𝙇𝘼 𝙄𝙋: ")
          par = parametros.split(",")
          for x in par:
              print(x.upper(), ":")
              print(ip_scraping(ip)[x])
              print("n")
              
    
              
              
elif choice == 5:
     print("\033[;32m")
     class GetHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header(
            'Content-Type',
            'text/plain; charset=utf-8',
            )
            self.send_header(
            'Last-Modified',
            self.date_time_string(time.time())
            )
    

            self.end_headers()
            self.wfile.write((text).encode('utf-8'))
     IP = ""
     IP = input("ingresa tu direccion IP, si no quieres solo pon 'localhost': ")
     print("para entrar al server busca en gogle 'localhost:8443 o si pusiste tu ip solo cambias el localhost por la IP")
     text = ""
     text = input ("ingresa el contenido del server:")
     if __name__ == '__main__':
         from http.server import HTTPServer
         server = HTTPServer(( (IP), 8443,), GetHandler)
     try:
        print("coneccion exitosa :)")
        sleep(1)
        print("te doy la bienvenida a mi server")
        sleep(1)
        print("la coneccion esta avierta...")
        server.serve_forever()
     except:
        print("ERROR :(")
        
        
elif choice == 6:
        def extract_ip():
            st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                st.connect(('10.255.255.255', 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                st.close()
            return IP
        print(extract_ip())



elif choice == 7:
     IP = ""
     IP = input("PONGA LA IP:")
     ADDRESSES = [IP]
     for ip in ADDRESSES:
         addr = ipaddress.ip_address(ip)
         print('{!r}'.format(addr))
         print('   IP version:', addr.version)
         print('   is private:', addr.is_private)
         print('  packed form:', binascii.hexlify(addr.packed))
         print('      integer:', int(addr))
         print()
     
     
elif choice == 8:

    os.system("clear")
   
    api_key = '31e04799e5b72d22be4bed51565ddadb'
    number = int(input("Numero de telefono: "))
    data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))
    for key, value in data.json().items():
        print("%s: %s" % (key, value))
   
 
elif choice == 9:
    
    
    g = int(input("1.-barrido grande\n2.-barrido a solo puertos basicos (21, 22, 25, 80)\nEnter Choice : ")) 
    
    
    if g == 1:
        
        print("\033[32;1m")
        
        ip = input("Ingresa la IP: ")
        ipDividida = ip.split('.')
        try:
            red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
            comienzo = int(input("Ingresa el número de comienzo de la subred: "))
            fin = int(input("Ingresa el número en el que deseas acabar el barrido: "))
            print ("[#] el barrido puede tardar segun la ip")
        except:
            print("[!] Error")
            sys.exit(1)
            
            
        if (platform.system()=="Windows"):
            ping = "ping -n 1"
        else :
            ping = "ping -c 1"
            tiempoInicio = datetime.now()
            print("[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin))
            for subred in range(comienzo, fin+1):
                direccion = red+str(subred)
                response = os.popen(ping+" "+direccion)
                for line in response.readlines():
                    if ("ttl" in line.lower()):
                        print(direccion,"está activo")
                        break
        tiempoFinal = datetime.now()
        tiempo = tiempoFinal - tiempoInicio
        print("[*] El escaneo ha durado %s"%tiempo)()
        
  
        quit()
      
    
    elif g == 2:
        
            print (" puede que este programa no funcione, si no funciona elija el barrido grande")
            IP = ""
            IP = input ("IP del escaneo :")
            def scan(addr, port):
                socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = socket_obj.connect_ex((addr,port)) 
                socket_obj.close()
                return result
            ports=[21, 22, 25, 80]
            for i in range(1,255):
                addr=(IP).format(i)
                for port in ports:
                    result=scan(addr, port)
                    if result==0:
                        print(addr, port, "OK")
                    else:
                        print(addr, port, "Failed")      
                        
                          

 
