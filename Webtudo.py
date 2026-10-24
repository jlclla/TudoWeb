# =====================================================================
# SISTEMA DE PESQUISA DE SATISFAÇÃO - TUDO WEB
# =====================================================================

TOTAL_ENTREVISTADOS_FINAL = 50 # Total de entrevistados na pesquisa final
teste_inicial = 10  # Teste com 10 entrevistados

# Contadores da ETAPA 1 (Teste Inicial)
qtd_excelente_teste = 0
qtd_bom_teste = 0
qtd_ruim_teste = 0

# Contadores GERAIS / FINAIS (Acumulam os 50 entrevistados)
qtd_excelente_total = 0
qtd_bom_total = 0
qtd_ruim_total = 0


# =====================================================================
# ETAPA 1: TESTE COM 10 ENTREVISTADOS
# =====================================================================
print("=" * 50)
print(f" Sistema de Pesquisa - TUDO WEB (ETAPA 1: {teste_inicial} clientes)")
print("=" * 50 + "\n")

for i in range(1, teste_inicial + 1):
    print(f"--- Entrevistado {i} de {teste_inicial} ---")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Acesso negado! Menor de 18 anos.\n")
        continue 
    
    print("Acesso permitido!")
    print("Qual o seu grau de satisfação com os serviços?")
    print("  [1] EXCELENTE")
    print("  [2] BOM")
    print("  [3] RUIM")

    opiniao = input("Digite o número correspondente à opinião (1, 2 ou 3): ")

    if opiniao == "1":
        qtd_excelente_teste += 1
        qtd_excelente_total += 1
        print("-> Resposta registrada com sucesso!\n")
    elif opiniao == "2":
        qtd_bom_teste += 1
        qtd_bom_total += 1
        print("-> Resposta registrada com sucesso!\n")
    elif opiniao == "3":
        qtd_ruim_teste += 1
        qtd_ruim_total += 1
        print("-> Resposta registrada com sucesso!\n")
    else:
        print("-> Opção inválida! Resposta não registrada.\n")

# Exibição do Resultado Parcial do Teste

print("\n" + "=" * 50)
print("             RESULTADO TESTE DA PESQUISA (10)           ")
print("=" * 50)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente_teste}")
print(f"b) Quantidade de respostas 'BOM':       {qtd_bom_teste}")
print(f"c) Quantidade de respostas 'RUIM':      {qtd_ruim_teste}")
print("=" * 50 + "\n")

input("Pressione ENTER para continuar para a Pesquisa Final (Até 50)...")



# ETAPA 2: PESQUISA FINAL (Continuando do 11 até 50)

print("\n" + "=" * 50)
print(f" Sistema de Pesquisa - TUDO WEB (ETAPA FINAL: {TOTAL_ENTREVISTADOS_FINAL} clientes)")
print("=" * 50 + "\n")

# Começa do 11 e vai até o 50
for i in range(teste_inicial + 1, TOTAL_ENTREVISTADOS_FINAL + 1):
    print(f"--- Entrevistado {i} de {TOTAL_ENTREVISTADOS_FINAL} ---")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Acesso negado! Menor de 18 anos.\n")
        continue 
    
    print("Acesso permitido!")
    print("Qual o seu grau de satisfação com os serviços?")
    print("  [1] EXCELENTE")
    print("  [2] BOM")
    print("  [3] RUIM")

    opiniao = input("Digite o número correspondente à opinião (1, 2 ou 3): ")

    if opiniao == "1":
        qtd_excelente_total += 1
        print("-> Resposta registrada com sucesso!\n")
    elif opiniao == "2":
        qtd_bom_total += 1
        print("-> Resposta registrada com sucesso!\n")
    elif opiniao == "3":
        qtd_ruim_total += 1
        print("-> Resposta registrada com sucesso!\n")
    else:
        print("-> Opção inválida! Resposta não registrada.\n")



# RESULTADOS FINAIS DA PESQUISA (Total de 50)

print("\n" + "=" * 50)
print("             RESULTADO FINAL DA PESQUISA (50)           ")
print("=" * 50)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente_total}")
print(f"b) Quantidade de respostas 'BOM':       {qtd_bom_total}")
print(f"c) Quantidade de respostas 'RUIM':      {qtd_ruim_total}")
print("=" * 50)