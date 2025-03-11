class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        """Adiciona um item ao topo da pilha."""
        self.itens.append(item)

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if not self.esta_vazia():
            return self.itens.pop()
        return None  # Retorna None se a pilha estiver vazia

    def peek(self):
        """Retorna o item do topo da pilha sem removê-lo."""
        if not self.esta_vazia():
            return self.itens[-1]
        return None  # Retorna None se a pilha estiver vazia

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o número de elementos na pilha."""
        return len(self.itens)

    def __str__(self):
        """Representação da pilha como string."""
        return f"Pilha: {self.itens}"


# Exemplo de uso
pilha = Pilha()
pilha.push(10)
pilha.push(20)
pilha.push(30)

print(pilha)         # Pilha: [10, 20, 30]
print(pilha.peek())  # 30 (Topo da pilha)
print(pilha.pop())   # Remove e retorna 30
print(pilha)         # Pilha: [10, 20] 