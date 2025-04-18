# \ a barra invertida é um caractere de escape
# . corresponde a qualquer caractere
# \d corresponde a qualquer dígito (0-9)
# \D corresponde a qualquer caractere que não seja um dígito
# \w corresponde a qualquer caractere alfanumérico
# \W corresponde a qualquer caractere que não seja alfanumérico
# \s corresponde a qualquer espaço em branco
# \S corresponde a qualquer caractere que não seja um espaço em branco

# [abc]
# [a-zA-Z] corresponde a qualquer letra minúscula ou maiúscula
# [0-9] corresponde a qualquer dígito
# [a-zA-Z0-9] corresponde a qualquer letra ou dígito

# * corresponde a zero ou mais ocorrências do caractere anterior
# + corresponde a uma ou mais ocorrências do caractere anterior
# ? corresponde a zero ou uma ocorrência do caractere anterior
# {n} corresponde exatamente a n ocorrências do caractere anterior
# {n,} corresponde a n ou mais ocorrências do caractere anterior
# {n,m} corresponde a entre n e m ocorrências do caractere anterior

# import re
# re.findall() encontra todas as ocorrências da expressão regular na string
# re.search() encontra a primeira ocorrência da expressão regular na string
# re.match() encontra a primeira ocorrência da expressão regular no início da string
# re.sub() substitui todas as ocorrências da expressão regular na string
# re.split() divide a string em uma lista de substrings com base na expressão regular
# re.compile() compila a expressão regular em um objeto de expressão regular


# \(\d{2}\)\s\d{4,5}-\d{4}  # Expressão regular para telefone
# \ caractere de escape
# \d{2} dois dígitos
# \s espaço em branco
# \d{4,5} quatro ou cinco dígitos
# \d{4} quatro dígitos
