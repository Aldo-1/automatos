automato = {
  'q0':{'a':['q0','q1'], 'b':['q0']},
  'q1':{'a':[''], 'b':['q2']},
  'q2':{'a':[''], 'b':['']}
} 

##Transforma de array para string
def __transformArrayToString__(novoAutomato, palavras):
  for estado in novoAutomato:
    for palavra in palavras:
      paraOndeVai = novoAutomato[estado][palavra]
      novoAutomato[estado][palavra] = ','.join(paraOndeVai)
  return novoAutomato

##aqui ele checa se tem espaco vazio e retorna true ou false
def __checkEmptySpace__(resultado):
  for letra in resultado:
    if(letra == ''):
      return True
    else:
      return False

##iniciar o estado inicial
def __initInicialState__(automato, palavras, estadoInicial, novoAutomato):
  for palavra in palavras:
    novoEstados =  ','.join(automato[estadoInicial][palavra])
    novoAutomato[estadoInicial][palavra] = {}
    novoAutomato[estadoInicial][palavra] = automato[estadoInicial][palavra]   
    if(novoEstados != estadoInicial):
      novoAutomato[novoEstados] = {}
    else:
      continue
  return novoAutomato

##checar se e aceito
def __checkIsAccepted__(automato:dict,estadoInicial, estadoFinal,palavra):
      #Iniciando o estado inicial
      estado = estadoInicial
      #Para cada letra do palavra
      for letra in palavra:
        if(not(letra in automato[estado])):
          print('algum caracter da palavra nao existe no alfabeto dessa maquina!')
          break
        else:
          estado = automato[estado][letra]
      ##Para ver se o estado final esta no conjunto do estado final.
      for ultimoEstado in estadoFinal:
        if(ultimoEstado in estado):
          return 'accept'
        else:
          return 'reject'  

##Transformar ndfa para dfa
def transform(automato, palavras, estadoInicial, estadoFinal, novoAutomato = {}):
  novoAutomato[estadoInicial] = {}
  ##Preencher o estado inicial que a partir dele iremos para os outros.
  novoAutomato = __initInicialState__(automato, palavras, estadoInicial, novoAutomato)
  visitados = []
  ##Enquanto o tamanho do vetor de resultados for diferente do tamanho do novo automato - 1
  ##Coloquei o -1 por conta que ele pula o estado inicial
  while(len(visitados) != (len(novoAutomato) - 1)):
    ##Aqui é para pegar o estado que vai virar o estado do automato e
    ##Pegar os respectivos resultados do alfabeto de cada um
    for estado in novoAutomato:
      ##Aqui eu verfico se ele é diferente do estado e inicial e 
      ##Se nao foi visitado, no array
      if(estado != estadoInicial and not(estado in visitados)):
        for palavra in palavras:
          ##Crio um array na posicao do estado e da palavra 
          novoAutomato[estado][palavra] = []
          ##Pego cada estado 1 de cada
          arraySplit = estado.split(',')
          ##Exemplo = 0,1
          ##Aqui é para juntar o conjunto por exemplo 0 quando recebe a vai para q0
          ##Quando recebe 1 vai para q1q2
          ##Agora eles juntam q0q1q2
          for unicoEstado in arraySplit:
            resultado = automato[unicoEstado][palavra]
            if(__checkEmptySpace__(resultado)):
              continue
            else:
              novoAutomato[estado][palavra].extend(resultado)   
        visitados.append(estado)    
    
    ##Aqui é para criar o estado dele no automato  
    for estado in visitados:
        for palavra in palavras:
          novoEstado = ','.join(novoAutomato[estado][palavra])
          if(novoEstado in novoAutomato):
            continue
          else:
            novoAutomato[novoEstado] = {}

  #aqui faco a transicao de array para como faco o finitio        
  
  novoAutomato = __transformArrayToString__(novoAutomato, palavras)
  return novoAutomato



novoAutomato = transform(automato,['a','b'], 'q0', {'q2'})

print(novoAutomato)
print(__checkIsAccepted__(novoAutomato, 'q0', {'q2'}, 'ab'))

