import os

'''
Funções matemáticas dos programa
'''
def getInputs():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    
    return (A, B)

def soma():
    A, B = getInputs()
    return A + B

def multiplica():
    A, B = getInputs()
    return A * B

def exp():
    A, B = getInputs()
    return A**B

def menos():
    A, B = getInputs()
    return A - B

#parte principal do programa
if __name__ == '__main__':
    opt = ''

    while True:
        os.system('cls')

        print("################MENU####################")
        print("# 1 - SOMA                             #")
        print("# 2 - MULTIPLICAÇÃO                    #")
        print("# 3 - EXPONENCIAL                      #")
        print("# 4 - SAIR                             #")
        print("# 5 - MENOS                            #")
        print("########################################")
        opt = int(input("Digite sua Opção: "))

        resultado = 0
        match opt:
            case 1: resultado = soma()
            case 2: resultado = multiplica()
            case 3: resultado = exp() 
            case 4: exit(0)
            case 5: resultado = menos()
        
        print('Resultado: ', resultado)
        os.system('pause')