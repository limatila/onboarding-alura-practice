valid_protocols = ['https://', 'http://']
valid_domains = ['.com', '.net', '.gov.br', '.br']

has_valid_protocol, has_valid_domain = False, False

user_url = input("Digite a URL para validação\t->")

for protocol in valid_protocols:
    if user_url.startswith(protocol):
        has_valid_protocol = True
        break

for domain in valid_domains:
    if domain in user_url:
        has_valid_domain = True
        break

if has_valid_protocol and has_valid_domain:
    print("URL válida!")
else:
    print("URL inválida!")
