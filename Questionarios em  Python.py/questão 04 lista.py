'''
Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado"
'''

#Método .remove() + condicionais if e else

livros = ["romance", "religião", "politica"]
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("livro encontrado")
else:
    print("Livro não encontrado")
print(livros)