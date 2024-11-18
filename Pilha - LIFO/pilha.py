class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.prox = None  # Ponteiro para o próximo livro na pilha

class PilhaDeLivros:
    def __init__(self):
        self.topo = None  # Representa o topo da pilha

    def empilhar(self, livro):
        """
        Adiciona um livro ao topo da pilha.
        """
        if not isinstance(livro, Livro):
            raise ValueError("O objeto deve ser uma instância da classe Livro.")
        livro.prox = self.topo  # O próximo livro será o atual topo
        self.topo = livro  # Atualiza o topo da pilha

    def desempilhar(self):
        """
        Remove e retorna o livro do topo da pilha.
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia, não é possível desempilhar.")
        livro_removido = self.topo
        self.topo = self.topo.prox  # Atualiza o topo para o próximo livro
        return livro_removido

    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        """
        return self.topo is None

    def mostrar_topo(self):
        """
        Retorna o livro no topo da pilha sem removê-lo.
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")
        return self.topo

    def exibir_pilha(self):
        """
        Exibe todos os livros da pilha.
        """
        if self.esta_vazia():
            print("A pilha está vazia.")
            return
        atual = self.topo
        while atual:
            print(f"Título: {atual.titulo}, Autor: {atual.autor}, Páginas: {atual.paginas}")
            atual = atual.prox

# Exemplo de uso
pilha = PilhaDeLivros()

# Criando livros
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1200)
livro2 = Livro("1984", "George Orwell", 328)
livro3 = Livro("O Hobbit", "J.R.R. Tolkien", 310)

# Empilhando livros
pilha.empilhar(livro1)
pilha.empilhar(livro2)
pilha.empilhar(livro3)

# Exibindo a pilha
print("Pilha de livros:")
pilha.exibir_pilha()

# Mostrando o topo
print("\nLivro no topo:")
topo = pilha.mostrar_topo()
print(f"Título: {topo.titulo}, Autor: {topo.autor}, Páginas: {topo.paginas}")

# Desempilhando um livro
print("\nDesempilhando livro...")
desempilhado = pilha.desempilhar()
print(f"Livro removido: {desempilhado.titulo}")

# Exibindo a pilha após desempilhar
print("\nPilha após desempilhar:")
pilha.exibir_pilha()
