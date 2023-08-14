def cent_metros(centimetros):
    metros = centimetros / 100
    return metros

def main():
    centimetros = float(input("Digite a medida em centímetros: "))
    metros = cent_metros(centimetros)
    print(f"{centimetros:.2f} centímetros é igual a {metros:.2f} metros.")   

if __name__ == "__main__":
    main()