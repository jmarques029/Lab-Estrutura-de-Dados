def two_sum(numeros, alvo):
    mapa = {}  
    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual  
        
        if complemento in mapa:         
            return [mapa[complemento], i] 
        
        mapa[valor_atual] = i             

if __name__ == "__main__":
    numeros = [2, 7, 11, 15]
    alvo = 9
    resultado = two_sum(numeros, alvo)
    print(resultado)  # saída esperada: [0, 1]