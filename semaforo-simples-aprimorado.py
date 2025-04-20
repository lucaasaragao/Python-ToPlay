import time

def main():
    semaforoAtivo = True
    statusAtual = "atencao forte"
    print("Iniciando...")

    while semaforoAtivo:
        statusAtual = "fechado"
        print("O status atual do semáforo é: " + str(statusAtual))
        time.sleep(5)

        statusAtual = "aberto"
        print("O status atual do semáforo é: " + str(statusAtual))
        time.sleep(5)
        
        statusAtual = "atencao"
        print("O status atual do semáforo é: " + str(statusAtual))
        time.sleep(3)
        
    
# Chamada direta
main()

