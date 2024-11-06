# Definindo o Nó ou Node
class Node:
    def __init__(self, data) -> None:
        self.data = data # o valor armazenado 
        self.next = None # Poteiro para o proximo nó, começa como None

class LinkedList: 
    def __init__(self) -> None:
        self.head = None # A lista começa vazia, então head é None

    def append(self,data):
        """Adiciona um novo nó/Node"""
        new_node = Node(data) #Cria um novo nó com o dado fornecido 

        if not self.head: #se a lista estiver vazia
            self.head = new_node #O novo npo serpa o primeiro da lista 
            return
        
        #Caso contrário, percorre até o último nó e adcinona o novo nó
        current = self.head
        while current.next:
            current = current.next 
        current.next = new_node
        #teste da main 