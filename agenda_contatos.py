def adicionar_contatos(contatos, nome, telefone, email):

  contato = {"Nome": nome.strip(), "Telefone": telefone.strip(), "Email": email.strip(), "favorito": False} 
  contatos.append(contato)
  print(f"\nO contato {nome} foi salvo com sucesso.")
  return

def Ver_Contato(contatos):
  print("\nLista de Contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "★" if contato ["favorito"] else " "
    print(f"{indice}. [{status}] Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}") 
  return    

def Editar_contato(contatos, indice_contato):
  indice_contato_editado = int(indice_contato) -1 
  if indice_contato_editado >= 0 and indice_contato_editado < len(contatos):
    contato = contatos[indice_contato_editado]
    opcao = input("qual opção você deseja alterar? (Nome/Telefone/Email): ").strip().capitalize()
    if opcao in contato:
      novo_valor = input(f"Digite o novo dado {opcao}: ").strip()
      contato [opcao] = novo_valor.strip()
      print(f"{opcao} do contato atualizado para {novo_valor}")
    else: 
      print("campo inválido")
  else:
    print("índice inválido")
    return

def Favoritar_Contato(contatos, indice_contato):
  indice_contato_editado = int(indice_contato) - 1
  contatos [indice_contato_editado]['favorito'] = True
  print(f"Contato {indice_contato} marcado como favorito!")
  return
  
def Desfavoritar_Contato(contatos, indice_contato):
  indice_contato_editado = int(indice_contato) - 1
  contatos [indice_contato_editado] [ "favorito"] = False
  print(f"Contato {indice_contato} desmarcado como favorito!")
  return

def Ver_Contatos_Favoritos(contatos):
  print("\nLista de Contatos Favotiros")
  encontrar = False
  for indice, contato in enumerate(contatos, start=1):
    if contato ['favorito']:
      status = "★" 
      print (f"{indice}. [{status}] Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}") 
      encontrar = True
    if not encontrar:
      print("Não há contatos na lista de Favoritos.")
    return

def Deletar_contatos(contatos, indice_contato):
    indice = int(indice_contato) - 1
    if indice >= 0 and indice < len(contatos):
      deletar = contatos.pop(indice) 
      print(f"Contato {deletar['Nome']} deletado com sucesso.")
    else:
      print("indice invalido")
    return
    
contatos = []

while True:
  print("\nLista de Contatos")
  print("1. Adicionar Contatos")
  print("2. Ver Lista de Contatos")
  print("3. Editar Contatos")
  print("4. Marcar Como Favorito")
  print("5. Desmarcar Como Favorito")
  print("6. Lista de Contatos Favoritos")
  print("7. Deletar Contatos")
  print("8. sair")

  escolha = input("Digite a sua escolha: ")
  if escolha == "1":
    dados = input("Digite Nome, Telefone e Email seperados por vírgula:")
    nome, telefone, email = dados.split(",")
    print("Nome:", nome)
    print("Telefone:", telefone)
    print("Email:", email)
    adicionar_contatos(contatos, nome, telefone, email)

  elif escolha == "2":
    Ver_Contato(contatos)

  elif escolha == "3":
    Ver_Contato(contatos)
    indice_contato = input("Digite o contato que deseja editar: ")
    Editar_contato(contatos, indice_contato)
  
  elif escolha =="4":
    Ver_Contato(contatos)
    indice_contato = input("Digite o indice que quer marcar como favorito: ")
    Favoritar_Contato(contatos, indice_contato)

  elif escolha == "5":
    Ver_Contato(contatos)
    indice_contato = input("Digite o indice do contato que deseja remover dos Favoritos:" )
    Desfavoritar_Contato(contatos, indice_contato)

  elif escolha == "6":
    Ver_Contatos_Favoritos(contatos)

  elif escolha == "7":
    Ver_Contato(contatos)
    indice_contato = input("Digite o indice do contato que deseja deletar: ")
    Deletar_contatos(contatos, indice_contato)    


  elif escolha == "8":
    print("Programa finalizado")

