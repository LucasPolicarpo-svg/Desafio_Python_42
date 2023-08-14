def calculo_quadrado(lado):
    area = lado * lado
    return area

def calculo_retangulo(base, altura):
    area = base * altura
    return area

def main():
    print("Escolha a forma geométrica que deseja")
    print("Tipo 1: Quadrado")
    print("Tipo 2: Retângulo")

    escolha = int(input("Digite o número da opção: "))

    if escolha == 1:
        lado = float(input("Digite o valor do lado do quadrado,(lembrando que estamos utilizando metros como parâmetros)? "))
        area = calculo_quadrado(lado)
        print(f"A área do quadrado é {area:.2f} M².")
    elif escolha == 2:
        base = float(input("Digite o valor da base do retângulo,(lembrando que estamos utilizando metros como parâmetros): "))
        altura = float(input("Digite o valor da altura do retângulo: "))
        area = calculo_retangulo(base, altura)
        print(f"A área do retângulo é {area:.2f} M².")
    else:
        print("Opção invalida!")
    
if __name__ == "__main__":
    main()