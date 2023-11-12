import os

def clear():
    os.system('cls')
    
def pedir_notas(trimestre):
    notas = {}
    materias = ["Matemática", "Química", "Inglês", "Português", "Geografia", "História", "Geometria", "Impactos", "Linguagem", "Inovação", "Modelagem", "Monitoramento"]
    
    for materia in materias:
        nota = float(input(f"{materia} ({trimestre}): "))
        clear()
        notas[materia] = nota
        
    return notas
print("Bem-vindo à calculadora de notas!")

while True:
    input("Pressione enter para continuar.")
    clear()
    
    print("Vamos coletar as notas do 1° trimestre.")
    notas1 = pedir_notas("1° trimestre")
    
    print("Agora as notas do 2° trimestre")
    notas2 = pedir_notas("2° trimestre")
    
    terceiro_trimestre = input("Você já recebeu as notas do 3° trimestre? s/n ")
    
    if terceiro_trimestre.lower() == 's':        
        notas3 = pedir_notas("3° trimestre")
        
        #Soma
        somas = {}
        for materia in notas1.keys():
            somas[materia] = notas1[materia] + notas2[materia] + notas3[materia]
    
        #Verificação
        for materia, soma in somas.items():
            if soma >= 18:
                print(f"Você passou em {materia} com {soma} pontos.")
            else:
               print(f"Ainda faltam {18 - soma} para passar em {materia}.")
    
    elif terceiro_trimestre.lower() == 'n':
        
        #Soma 2
        somas = {}
        for materia in notas1.keys():
            somas[materia] = notas1[materia] + notas2[materia]
        
        #Verificação 2
        for materia, soma in somas.items():
            if soma >= 18:
                print(f"Você passou em {materia} com {soma} pontos.")
            else:
                print(f"Ainda faltam {18 - soma} para passar em {materia}.")
    
    else:
        print("Digite 's' para sim ou 'n' para não.")
        
    sair = input("Você deseja sair? ")
    if sair.lower() == 's':
        break
    else:
        continue
    

    