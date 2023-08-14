def main():
    produtos = []  #essa é a lista onde vai ser armazenados os produtos.

    while True:  #esse é a repetição que garante que o sitema continue executando e voltando até que digite "sair".

        codigo = input("Digite o codigo do produto, ou 'sair' para encerrar: ")

        if codigo.lower() == 'sair':
            break

        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço do produto: "))

        # calcula o valor total da compra
        total = quantidade * preco

        # faz a função de adcionar os itens digitados a lista de produtos
        produtos.append({
            'codigo': codigo,
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
            'valor_total': total
        })

    # esse print ai exibir as informações dos produtos que cadastrou e o valor total que foi feito da compra.
    print("\nProdutos cadastrados: ")

    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}, Valor Total: R${produto['valor_total']:.2f}")

    total_compra = sum(produto['valor_total'] for produto in produtos)

    print(f"Valor total da compra: R$ {total_compra:.2f}")   

#validação se a função esta sendo chamada do jeito certo.
if __name__ == "__main__":
    main()




