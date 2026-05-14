def two_sum_brute_force(nums, target):
    # Percorre cada elemento da lista pelo seu índice
    for i in range(len(nums)):
        # Percorre os elementos seguintes ao índice 'i'
        for j in range(i + 1, len(nums)):
            # Verifica se a soma dos dois elementos é igual ao alvo
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # Caso nenhum par seja encontrado, retorna uma lista vazia
    return []

def test_two_sum_brute_force():
    # Teste 1 - Caso clássico
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum_brute_force(nums, target)
    print(f"Teste 1: {result} - Esperado: [0, 1] ou [1, 0]")

    # Teste 2 - Números negativos
    nums = [-3, 4, 3, 90]
    target = 0
    result = two_sum_brute_force(nums, target)
    print(f"Teste 2: {result} - Esperado: [0, 2] ou [2, 0]")

    # Teste 3 - Repetição de números
    nums = [3, 3]
    target = 6
    result = two_sum_brute_force(nums, target)
    print(f"Teste 3: {result} - Esperado: [0, 1] ou [1, 0]")

    # Teste 4 - Números com zero
    nums = [0, 4, 3, 0]
    target = 0
    result = two_sum_brute_force(nums, target)
    print(f"Teste 4: {result} - Esperado: [0, 3] ou [3, 0]")

    # Teste 5 - Target negativo
    nums = [-1, -2, -3, -4, -5]
    target = -8
    result = two_sum_brute_force(nums, target)
    print(f"Teste 5: {result} - Esperado: [2, 4] ou [4, 2]")

    # Teste 6 - Target positivo, números mistos
    nums = [1, -2, 3, 5, -4, 8]
    target = 4
    result = two_sum_brute_force(nums, target)
    print(f"Teste 6: {result} - Esperado: [0, 2] ou [2, 0]")

    # Teste 7 - Não existe par
    nums = [1, 2, 3]
    target = 10
    result = two_sum_brute_force(nums, target)
    print(f"Teste 7: {result} - Esperado: []")

    # Teste 8 - Par é o menor e maior elemento
    nums = [1, 5, 10, 20, 50]
    target = 51
    result = two_sum_brute_force(nums, target)
    print(f"Teste 8: {result} - Esperado: [0, 4] ou [4, 0]")

    # Teste 9 - Par adjacente
    nums = [1, 2, 3, 4, 5]
    target = 7
    result = two_sum_brute_force(nums, target)
    print(f"Teste 9: {result} - Esperado: [2, 4] ou [3, 2] (Nota: 3+4=7)")

    # Teste 10 - Par nos extremos
    nums = [5, 1, 2, 3, 5]
    target = 10
    result = two_sum_brute_force(nums, target)
    print(f"Teste 10: {result} - Esperado: [0, 4] ou [4, 0]")

# Chama a função de testes
test_two_sum_brute_force()