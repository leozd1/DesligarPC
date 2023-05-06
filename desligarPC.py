import os
import time
from datetime import datetime, time as t

# Defina a hora em que deseja desligar o computador
hora_desligar = input("Digite a hora em que deseja desligar o computador (hh:mm:ss): ")

# Converte a hora para um objeto datetime
hora_desligar = datetime.strptime(hora_desligar, "%H:%M:%S").time()

# Obtém a hora atual como um objeto time
hora_atual = datetime.now().time()

# Calcula o tempo restante até a hora de desligar em segundos
tempo_restante = (datetime.combine(datetime.today(), hora_desligar) - datetime.combine(datetime.today(), hora_atual)).total_seconds()

# Espera até a hora definida para desligar o computador
time.sleep(tempo_restante)

# Desliga o computador
if os.name == "nt":
    os.system("shutdown /s /t 1")
elif os.name == "posix":
    os.system("sudo shutdown -h now")
else:
    print("Sistema operacional não suportado.")