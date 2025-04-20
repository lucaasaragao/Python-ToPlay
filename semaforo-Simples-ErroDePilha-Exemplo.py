import time

def statusDoSemaforo(statusAtual):
    print("O status atual do semáforo é: " + str(statusAtual))
    statusAtual = fecharSemaforo(statusAtual)
    time.sleep(1)
    return statusAtual
    
def fecharSemaforo(statusAtual):
    time.sleep(5)
    statusAtual = "fechado"
    print("O status atual do semáforo é: " + str(statusAtual))
    return abrirSemaforo(statusAtual)

def abrirSemaforo(statusAtual):
    time.sleep(5)
    statusAtual = "aberto"
    print("O status atual do semáforo é: " + str(statusAtual))
    return atencaoSemaforo(statusAtual)

def atencaoSemaforo(statusAtual):
    time.sleep(2)
    statusAtual = "atencao"
    print("O status atual do semáforo é: " + str(statusAtual))
    return fecharSemaforo(statusAtual)
    
def main():
    statusAtual = "atencao forte"
    print("Iniciando...")
    statusDoSemaforo(statusAtual) 

# Chamada direta
main()
