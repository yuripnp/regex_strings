import re

texto_email = """
Olá. senhores, sou o Fulano de tal e meu e-mail é fulano@fulano.com 
e meu telefone é (11) 91234-5678.
Aguardo retorno.
Atenciosamente,"""

padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
padrao_telefone = r'\(\d{2}\) \d{5}-\d{4}'
padrao_telefone2 = r'\(\d{2}\) \d{4}-\d{4}'

validate = re.search(padrao_email, texto_email)
if validate:
    print(f"Email encontrado: {validate.group()}")
else:
    print("Email não encontrado.")
validate = re.search(padrao_telefone, texto_email)
if validate:
    print(f"Telefone encontrado: {validate.group()}")
else:
    print("Telefone não encontrado.")
validate = re.search(padrao_telefone2, texto_email)
if validate:
    print(f"Telefone encontrado: {validate.group()}")
else:  
    print("Telefone não encontrado.")
