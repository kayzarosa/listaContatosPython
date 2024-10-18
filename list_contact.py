def add_new_contact(contacts, name, phone, email, favorite):
  new_contact = {
    "nome": name,
    "telefone": phone,
    "email": email,
    "favorito": True if favorite == "1" else False
  }
  contacts.append(new_contact)
  print(f"O contato {name} foi adicionado com sucesso!")
  return

def view_list_contact(contacts, view_favorite = False):
  print("\nLista de contatos:")
  for index, contact in enumerate(contacts, start=1):
    if view_favorite == True and contact["favorito"] == False:
      continue
    favorite = "★" if contact["favorito"] else "☆"
    name = contact["nome"]
    phone = contact["telefone"]
    email = contact["email"]
    print(f"""{index} - {favorite} Nome: {name} | Telefone: {phone} | E-mail: {email}""")
  return

def edit_contact(contacts, index, name, phone, email):
  print("\nEditar contato.")
  if index <= 0 or index > len(contacts):
    print(f"Contato não encontrado!")
  else:
    contacts[index - 1]["nome"] = name
    contacts[index - 1]["telefone"] = phone
    contacts[index - 1]["email"] = email
    print(f"Contato {index} atualizada para {name}")
  return

def unfavorite_favorite(contacts, index):
  if index <= 0 or index > len(contacts):
    print(f"Contato não encontrado!")
  else:
    contacts[index - 1]["favorito"] = not(contacts[index - 1]["favorito"])
    name = contacts[index - 1]["nome"]
    favorite = "favoritado" if contacts[index - 1]["favorito"] else "desvaforitado"
    print(f"Contato {index} - {name} foi {favorite}")
  return

def delete_contact(contacts, index):
  if index <= 0 or index > len(contacts):
    print(f"Contato não encontrado!")
  else:
    contacts.remove(contacts[index -1])
    print("Contato removido com sucesso!")
  return

contacts = []
try:
  while True:
    print("\nMenu lista de contatos:")
    print("1. Adicionar um novo contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Favoritar/ Desavaforitar contato")
    print("5. Ver contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")
    
    option = int(input("Digite sua escolha: "))
    
    if option == 1:
      name = input("Digite o nome do contato: ")
      phone = input("Digite o número do telefone do contato: ")
      email = input("Digite o e-mail do contato: ")
      favorite = input("Favoritar contato \n1 - Sim \n2 - Não: ")
      add_new_contact(contacts, name, phone, email, favorite)
    
    elif option == 2:
      view_list_contact(contacts)
      
    elif option == 3:
      view_list_contact(contacts)
      index = int(input("Digite o número do contato: "))
      name = input("Digite o nome do contato: ")
      phone = input("Digite o número do telefone do contato: ")
      email = input("Digite o e-mail do contato: ")
      edit_contact(contacts, index, name, phone, email)
    
    elif option == 4:
      view_list_contact(contacts)
      print("\nDesfavoritar ou Favoritar contato:")
      index = int(input("Digite o número do contato: "))
      unfavorite_favorite(contacts, index)
      
    elif option == 5:
      view_list_contact(contacts, True)
    
    elif option == 6:
      view_list_contact(contacts)
      print("\nDeletar contato:")
      index = int(input("Digite o número do contato: "))
      delete_contact(contacts, index)
    
    elif option == 7:
      break
except Exception as e:
  print(f"Erro: {e}")
finally:
  print("Agenda finalizada!")
  