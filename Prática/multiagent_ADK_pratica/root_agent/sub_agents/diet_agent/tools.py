def build_diet_plan(
    dieta_tipo: str,
    refeicoes_dia: int,
    calorias_alvo: float,
    proteina_g: int,
    gordura_g: int,
    carbo_g: int,
) -> dict:
    base = [
        {"nome": "Café da manhã", "descricao": "Proteína + carbo simples + fruta"},
        {"nome": "Almoço", "descricao": "Arroz/mandioca + feijão + proteína + salada"},
        {"nome": "Lanche", "descricao": "Iogurte/fruta (ou equivalente) + oleaginosas"},
        {"nome": "Jantar", "descricao": "Proteína + carbo + legumes"},
    ]

    meals = base[:]
    while len(meals) < refeicoes_dia:
        meals.insert(-1, {"nome": "Lanche extra", "descricao": "Fruta + iogurte (ou equivalente) / sanduíche leve"})
    meals = meals[:refeicoes_dia]

    resumo = (
        f"Dieta {dieta_tipo}. Meta ~{calorias_alvo:.0f} kcal/dia "
        f"(P{proteina_g}g G{gordura_g}g C{carbo_g}g)."
    )

    return {"resumo": resumo, "refeicoes": meals}