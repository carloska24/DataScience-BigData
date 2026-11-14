# Aula 07 - Exercício 14: Desconto comercial para compra expressiva ou cliente VIP (Operador OR)
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 34)

'''
Enunciado:
Solicite o valor de uma compra e informe se o cliente é VIP. O cliente receberá 10% de desconto quando a compra for superior a R$ 500 ou ele for VIP.
'''

# 1. FUNÇÃO DE BENEFÍCIO COMERCIAL
def aplicar_desconto_vip(valor_compra: float, is_vip: bool):
    # Condição: compra > 500 OU cliente VIP
    tem_desconto = (valor_compra > 500.00) or is_vip
    
    taxa_desconto = 0.10 if tem_desconto else 0.00
    desconto = valor_compra * taxa_desconto
    valor_pago = valor_compra - desconto
    
    return {
        "valor_compra": valor_compra,
        "is_vip": is_vip,
        "tem_desconto": tem_desconto,
        "taxa_pct": taxa_desconto * 100,
        "desconto": desconto,
        "valor_pago": valor_pago
    }

# 2. TESTES DE CENÁRIOS
pedidos = [
    (350.00, False),  # Baixo valor e Não-VIP (False or False -> Sem desconto)
    (750.00, False),  # Alto valor e Não-VIP (True or False -> Desconto)
    (200.00, True),   # Baixo valor e VIP (False or True -> Desconto)
    (900.00, True)    # Alto valor e VIP (True or True -> Desconto)
]

print("=== AVALIAÇÃO DE DESCONTO VIP / VALOR ===")
for v, vip in pedidos:
    r = aplicar_desconto_vip(v, vip)
    tipo_cliente = "VIP" if vip else "Comum"
    status_desc = f"Recebe 10% de desconto (-R$ {r['desconto']:.2f})" if r['tem_desconto'] else "Sem desconto"
    print(f"Compra: R$ {v:6.2f} | Tipo: {tipo_cliente:5s} -> {status_desc} | Total a pagar: R$ {r['valor_pago']:6.2f}")

