cand1 = input("Insira o nome do candidato 1: ")
cand2 = input("Insira o nome do candidato 2: ")
cand3 = input("Insira o nome do candidato 3: ")

cand1 = cand1.upper()
cand2 = cand2.upper()
cand3 = cand3.upper()

nomeVoto = []
votoCandidato = []

candidatos = [cand1, cand2, cand3]

qtdVotos = input("Insira quantos eleitores irão votar na urna: ")


while qtdVotos.isnumeric() != True:
    qtdVotos = input("Insira quantos eleitores irão votar na urna: ")


def urnaEletronica(candidatos, qtdVotos):
    n = 0
    cand = ""
    nome = ""
    while n < qtdVotos:
        nome = input("Insira seu nome: ")
        nome = nome.upper()
        cand = input("Insira o nome do candidato a ser votado: ")
        cand = cand.upper()
        
        while cand != candidatos[0] and cand != candidatos[1] and cand != candidatos[2]:
            cand = input("Insira um nome valido de candidato: ")
            cand = cand.upper()
            
        nomeVoto.append(nome)
        votoCandidato.append(cand)
    
        print("Seu voto foi registrado com sucesso!\n ")    
        n+=1
    
urnaEletronica(candidatos, int(qtdVotos))
    
def contagemVotos(candidatos, votoCandidato):
    
    cont1 = votoCandidato.count(candidatos[0])
    cont2 = votoCandidato.count(candidatos[1])
    cont3 = votoCandidato.count(candidatos[2])
    
    print(f"Veja o resultado dos votos da urna:\n{candidatos[0]}: {cont1} votos\n{candidatos[1]}: {cont2} votos\n{candidatos[2]}: {cont3} votos\n")
    
    if cont1 > cont2 and cont1 > cont3:
        print(f"O candidato {candidatos[0]}, ganhou a eleição com {cont1} votos!")
    elif cont2 > cont3 and cont2 > cont1:
        print(f"O candidato {candidatos[1]}, ganhou a eleição com {cont2} votos!")
    elif cont3 > cont2 and cont3 > cont1: 
        print(f"O candidato {candidatos[2]}, ganhou a eleição com {cont3} votos!")
    elif cont1 == cont2 and cont2 == cont3:
        print(
            "Empate tecnico entre todos os participantes da eleição")
    elif cont1 == cont2 and cont2 > cont3:
        print(f"Empate tecnico entre os participantes {candidatos[0]} e {candidatos[1]} da eleição, haverá segundo turno!")
    elif cont1 == cont3:
        print(f"Empate tecnico entre os participantes {candidatos[0]} e {candidatos[2]} da eleição, haverá segundo turno!")
    elif cont2 == cont3:
        print(f"Empate tecnico entre os participantes {candidatos[1]} e {candidatos[2]} da eleição, haverá segundo turno!")
        
contagemVotos(candidatos, votoCandidato)    
