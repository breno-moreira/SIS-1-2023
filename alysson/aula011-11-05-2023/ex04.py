""" pragrama para imprimir uma agenda diaria , com horarios de 15 em 15 minutos 
EXEMPLO -- FOR dentro de for --- for alinhados!
0:0
0:15
0:30
0:45
1:0
1:15
1:30
1:45
2:00
...
23:45
"""
for hora in range(24):
    if hora == 0:
        hora = "00"
    for minuto in range(0,60,15):
        if minuto == 0:
            minuto = "00"
        print(f"{hora}:{minuto}")