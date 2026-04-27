# Sistema simples de análise de vendas

vendas = [
    {"produto": "Perfume", "valor": 150, "quantidade": 10},
    {"produto": "Base", "valor": 80, "quantidade": 15},
    {"produto": "Batom", "valor": 50, "quantidade": 20},
]

def calcular_faturamento(vendas):
    total = 0
    for venda in vendas:
        total += venda["valor"] * venda["quantidade"]
    return total

def produto_mais_vendido(vendas):
    mais_vendido = max(vendas, key=lambda x: x["quantidade"])
    return mais_vendido["produto"]

def ticket_medio(vendas):
    total_vendas = sum(v["quantidade"] for v in vendas)
    faturamento = calcular_faturamento(vendas)
    return faturamento / total_vendas

def gerar_relatorio():
    print("📊 RELATÓRIO DE VENDAS\n")
    print(f"Faturamento total: R$ {calcular_faturamento(vendas)}")
    print(f"Produto mais vendido: {produto_mais_vendido(vendas)}")
    print(f"Ticket médio: R$ {ticket_medio(vendas):.2f}")

if __name__ == "__main__":
    gerar_relatorio()
