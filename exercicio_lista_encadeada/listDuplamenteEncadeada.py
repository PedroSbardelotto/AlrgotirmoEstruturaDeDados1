class Node: 
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
        self.prev = None

class DoublyLinkedList: 
    def __init__(self) -> None:
        self.head = None

    def insert_in_order(self, data):
        # insere o node na lista em ordem alfabetica.
        new_node = Node(data)

        # Caso especial: Lista vazia ou novo nó deve ser o primeiro
        if not self.head or data < self.head.data:
            new_node.next = self.head # Aponta o novo nó para o head arual 
            if self.head: 
                self.head.prev = new_node
            self.head = new_node
            return
        
        #caso geral: inserir no meio ou no final da lista 
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        
        #Insere o novo nó após o nó atual 
        new_node.next = current.next
        if current.next: 
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

    def display(self):
        """Imprime os elementos da lista na ordem direta."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(elements))
    
    def display_reverse(self):
        """Imprime os elementos da lista na ordem inversa."""
        elements = []
        current = self.head
        # Acha o último nó
        while current and current.next:
            current = current.next
        # Coleta os elementos do final para o início
        while current:
            elements.append(current.data)
            current = current.prev
        print(" <- ".join(elements))

# Cria uma instância da lista duplamente encadeada
dll = DoublyLinkedList()

# Insere alguns elementos em ordem alfabética
dll.insert_in_order("banana")
dll.insert_in_order("apple")
dll.insert_in_order("cherry")
dll.insert_in_order("date")
dll.insert_in_order("fig")
dll.insert_in_order("grape")

# Exibe a lista na ordem direta
print("Lista em ordem alfabética:")
dll.display()

# Exibe a lista na ordem inversa
print("Lista em ordem inversa:")
dll.display_reverse()
