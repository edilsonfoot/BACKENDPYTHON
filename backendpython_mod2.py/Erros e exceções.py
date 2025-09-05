
#8.1. Erros de sintaxe
# Erros de sintaxe, também conhecidos como erros de parse, são provavelmente os mais frequentes entre aqueles que ainda estão aprendendo Python:


while True print('Olá mundo')
  File "<stdin>", line 1
    while True print('Olá mundo')
               ^^^^^
SyntaxError: invalid syntax

# O analisador sintático repete a linha ofensiva e exibe pequenas setas apontando para o local onde o erro foi detectado. Note que esse nem sempre é o local que precisa ser corrigido. No exemplo, o erro é detectado na função print(), já que dois pontos (':') estão faltando logo antes dele.

# O nome do arquivo (<stdin> no nosso exemplo) e o número da linha são impressos para que você saiba onde procurar caso a entrada tenha vindo de um arquivo.

# Exceções
# Mesmo que um comando ou expressão estejam sintaticamente corretos, talvez ocorra um erro na hora de sua execução. Erros detectados durante a execução são chamados exceções e não são necessariamente fatais: logo veremos como tratá-las em programas Python. A maioria das exceções não são tratadas pelos programas e acabam resultando em mensagens de erro:

10 * (1/0)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~

# TypeError: can only concatenate str (not "int") to str
# A última linha da mensagem de erro indica o que aconteceu. Exceções surgem com diferentes tipos, e o tipo é exibido como parte da mensagem: os tipos no exemplo são ZeroDivisionError, NameError e TypeError. A string exibida como sendo o tipo da exceção é o nome da exceção embutida que ocorreu. Isso é verdade para todas exceções pré-definidas em Python, mas não é necessariamente verdade para exceções definidas pelo usuário (embora seja uma convenção útil). Os nomes das exceções padrões são identificadores embutidos (não palavras reservadas).


try:
    raise Exception('spam', 'ovos')
except Exception as inst:
    print(type(inst))    # o tipo da exceção
    print(inst.args)     # argumentos armazenados em .args
    print(inst)          # __str__ permite imprimir args diretamente,
                         # mas pode ser substituído em subclasses de exceção
    x, y = inst.args     # desempacota args
    print('x =', x)
    print('y =', y)

<class 'Exception'>
('spam', 'ovos')
('spam', 'ovos')
x = spam
y = ovos
