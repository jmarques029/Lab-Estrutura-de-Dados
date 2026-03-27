# Ajuste os métodos abaixo psuh_aux, pop_aux e get_min para que # seja possível
# encontrar o elemento mínimo de uma pilha simplesmente buscando no topo (peek) da pilha min_stack.

from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        """
        Função para empilhar na pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        main_stack.push(data)
        
        if min_stack.is_empty():
            min_stack.push(data)
        else:
            if data <= min_stack.singly_linked_list.peek():
                min_stack.push(data)


    def pop_aux():
        """
        Função para desempilhar da pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        if main_stack.is_empty():
            return None
        
        removido = main_stack.pop()
        
        # Se o valor que saiu da principal é o que estava no topo da min_stack, ele sai de lá também
        if not min_stack.is_empty() and removido == min_stack.singly_linked_list.peek():
            min_stack.pop()
        
        return removido

    def get_min():
        """
        Função para retornar o mínimo atual.
        """
        if min_stack.is_empty():
            raise IndexError("Estrutura Vazia - Não há valor mínimo")

        return min_stack.singly_linked_list.peek()

    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")