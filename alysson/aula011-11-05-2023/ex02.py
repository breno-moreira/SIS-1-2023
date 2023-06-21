""" Pragrama para gerar a tabela de jogo de um campeonato que tem 5 
times (timnes jogam em casa do adversario)"""

print("="*50)
for time1 in ("SPF","ATL","VAS","GRE","PAR"):
    print(time1)
    for time2 in ("SPF","ATL","VAS","GRE","PAR"):
        if time1 != time2:
            print(f"{time1} x {time2}")

print("="*50)