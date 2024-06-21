import random
import os
import sys
import time
import webbrowser



def abrir_janelas():
    # lista de urls para o navegador abrir
    urls = [
    "https://www.google.com",
    "https://www.g1.globo.com",
    "https://www.uol.com.br",
    "https://www.google.com",
    "https://www.google.com",
    ]
# looping que roda 5 vezes

    for i in range(5):
        url = random.choice(urls)
        url = urls[i] 
        webbrowser.open(url)



def evento_aleatorio():
    opcoes = 6
    escolha_indesejada = random.randint(1, opcoes)

    try:
        escolha = int(input(f"escolha um numero entre 1 e {opcoes}"))
    except ValueError as e:
         print(f"entrada invalida: {e}. tente de novo!")
         evento_aleatorio()

    if escolha == escolha_indesejada:
        print('ops, ja era, voce perdeu!')

        abrir_janelas()
        time.sleep(5)

    # para windows
        if(sys.platform == 'win32'):
                os.system("shutdown /s /t 1")

            # para linux
        elif sys.plataform == 'linux' or sys.plataform == 'linux2':  
                os.system("shutdown now")

                # para mac
        elif sys.plataform == 'darwin':
                os.system("shutdown -h now")
                sys.exit()  
                
            #os.system("shutdown /s /t 1")
    else:
        print('voce esta seguro por enquanto!')
        evento_aleatorio()

evento_aleatorio()