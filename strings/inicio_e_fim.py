def analisar_url(url):
    inicia_com_https = url.startswith("https://")
    termina_com_br = url.endswith("br")

    return inicia_com_https, termina_com_br

url = "https://www.gov.br"
print(f"Utiliza 'https'? {analisar_url(url)[0]}")
print(f"Termina com .br? {analisar_url(url)[1]}")