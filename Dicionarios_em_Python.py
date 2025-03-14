meu_dicionario = {
    "nome": "Maria",
    "idade": 30,
    "profissao": "Engenharia"
    }

/////////////////////////////////////////////////////////////////////////////////
Criando um Dicionario

# Usando colchetes
meu_dicionario = {
    " cidade " : " S o Paulo " ,
    " populacao " : 12300000
}

# Usando dict ()
outro_dicionario = dict ( pais = " Brasil " ,
continente = " A m r i c a do Sul " )

/////////////////////////////////////////////////////////////////////////////////
Criando um Dicionario Vazio

# Criando um d i c i o n r i o vazio
dicionario_vazio = {}
print ( dicionario_vazio ) # S a i d a : {}

# Criando com a f u n o dict ()
dicionario_vazio = dict ()
print ( dicionario_vazio ) # S a i d a : {}

# Adicionando itens ao d i c i o n r i o
dicionario_vazio [ " chave1 " ] = " valor1 "
dicionario_vazio [ " chave2 " ] = 42
print ( dicionario_vazio ) # S a i d a : { ’ chave1 ’: ’ valor1 ’, ’ chave2 ’: 42}

/////////////////////////////////////////////////////////////////////////////////
Criando um Dicionario com Valores Iniciais

# Usando chaves {}
dicionario = {
 " nome " : " Carlos " ,
 " idade " : 28 ,
 " cidade " : " S o Paulo "
}
print ( dicionario )
# S a d a : { ’ nome ’: ’ Carlos ’, ’ idade ’: 28 , ’ cidade ’: ’ S o Paulo ’}

# Usando a f u n o dict ()
dicionario = dict ( nome = " Carlos " , idade =28 ,
cidade = " S o Paulo " )
print ( dicionario )
# S a d a : { ’ nome ’: ’ Carlos ’, ’ idade ’: 28 , ’ cidade ’: ’ S o Paulo ’}

/////////////////////////////////////////////////////////////////////////////////
Criando Dicionarios a Partir de Listas ou Tuplas

# Usando uma lista de pares
lista_pares = [( " nome " , " Ana " ) , ( " idade " , 25) ,
( " cidade " , " Rio " ) ]
dicionario = dict ( lista_pares )
print ( dicionario )
# S a d a : { ’ nome ’: ’ Ana ’, ’ idade ’: 25 ,’ cidade ’: ’ Rio ’}

# Usando uma tupla de pares
tupla_pares = (( " profissao " , " Engenheira " ) ,
( " salario " , 5000) )
dicionario = dict ( tupla_pares )
print ( dicionario )
# S a i d a : { ’ profissao ’: ’ Engenheira ’,’ salario ’: 5000}

/////////////////////////////////////////////////////////////////////////////////
Criando Dicionarios com Compreensão (dict comprehension)

# Criando um d i c i o n r i o de quadrados de n u m e r o s
quadrados = { x : x **2 for x in range (1 , 6) }
print ( quadrados )
# S a d a : {1: 1 , 2: 4 , 3: 9 , 4: 16 , 5: 25}

# Criando um d i c i o n a r i o com base em c o n d i c o e s
numeros_pares = { x : x *2 for x in range (1 , 6) if
x % 2 == 0}
print ( numeros_pares )
# S a d a : {2: 4 , 4: 8}

/////////////////////////////////////////////////////////////////////////////////
Erros Comuns ao Criar Dicionarios

# Tentando usar uma lista como chave ( ERRO )
# dicionario = {[1 , 2]: " valor "} # TypeError

# Chaves duplicadas
dicionario = { " a " : 1 , " b " : 2 , " a " : 3}
print ( dicionario )
# S a d a : { ’ a ’: 3 , ’b ’: 2}
# A chave ’a ’ foi sobrescrita

/////////////////////////////////////////////////////////////////////////////////
Acessando e Modificando Valores

dicionario = { " nome " : " Carlos " , " idade " : 25}

# Acessando um valor
print ( dicionario [ " nome " ]) # S a i d a : Carlos

# Modificando um valor
dicionario [ " idade " ] = 26
print ( dicionario [ " idade " ]) # S a i d a : 26

