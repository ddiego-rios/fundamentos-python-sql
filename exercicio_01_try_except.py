# exercicio_01_try_except.py
# Simulação de limpeza de dados: processar uma lista com erros de digitação

dados_brutos = ["25", "30", "N/A", "45", "erro_de_leitura", "50"]
dados_limpos = []
erros = 0

print("A iniciar a limpeza de dados...\n")

for valor in dados_brutos:
    try:
        # O programa TENTA converter o texto para número inteiro
        numero = int(valor)
        dados_limpos.append(numero)
        print(f"✅ Sucesso: '{valor}' convertido para {numero}")
    except:
        # Se a conversão falhar (ex: "N/A"), ele vem para aqui em vez de parar o programa
        erros += 1
        print(f"❌ Aviso: O valor '{valor}' não é um número válido e foi ignorado.")

print("\n--- Resumo da Operação ---")
print(f"Valores válidos guardados: {dados_limpos}")
print(f"Total de erros ignorados: {erros}")
