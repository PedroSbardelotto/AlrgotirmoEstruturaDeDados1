# Definindo o Nó ou Node
class Node:
    def __init__(self, data) -> None:
        self.data = data  # O valor armazenado
        self.next = None  # Ponteiro para o próximo nó, começa como None

class LinkedList:
    def __init__(self) -> None:
        self.head = None  # A lista começa vazia, então head é None

    def append(self, data):
        """Adiciona um novo nó ao final da lista"""
        new_node = Node(data)  # Cria um novo nó com o dado fornecido

        if not self.head:  # Se a lista estiver vazia
            self.head = new_node  # O novo nó será o primeiro da lista
            return

        # Caso contrário, percorre até o último nó e adiciona o novo nó
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Adiciona um novo nó no início da lista"""
        new_node = Node(data)
        new_node.next = self.head  # Aponta o novo nó para o antigo head
        self.head = new_node  # Atualiza o head para o novo nó

    def display(self):
        """Exibe todos os elementos da lista"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def delete(self, data):
        """Remove o primeiro nó com o valor especificado"""
        current = self.head

        # Caso especial: o nó a ser removido é o head
        if current and current.data == data:
            self.head = current.next
            return

        # Busca pelo nó a ser removido
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        # Se o nó foi encontrado, ajusta os ponteiros
        if current:
            previous.next = current.next

    def find(self, data):
        """Procura por um nó com o valor especificado"""
        current = self.head
        while current:
            if current.data == data:
                return True  # Encontrado
            current = current.next
        return False  # Não encontrado