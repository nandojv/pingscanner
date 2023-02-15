import platform
import subprocess
#platform.sistem per ping di qualsisiesi sistema operativo

ip = ""
so =platform.system()
#print(so)

if(so == "Linux"):
    stato,risultato=subprocess.getstatusoutput("ping  2" + ip)
    print (risultato)

if (so == "Windows"):
    stato, risultato = subprocess.getstatusoutput("ping -c 2" + ip)
    print(risultato)


