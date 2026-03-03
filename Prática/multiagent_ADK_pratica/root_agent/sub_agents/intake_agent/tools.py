from typing import Dict, Any

ACTIVITY_FACTORS = {
    "sedentario": 1.2,
    "leve": 1.375,
    "moderado": 1.55,
    "alto": 1.725,
    "atleta": 1.9,
}

def calc_bmr_harris_benedict_revised(sexo: str, peso_kg: float, altura_cm: float, idade: int) -> float:
    sexo = sexo.strip().upper()
    if sexo not in {"M", "F"}:
        raise ValueError("sexo deve ser 'M' ou 'F'.")
    if sexo == "M":
        return 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * idade)
    return 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * idade)

def calc_tdee(bmr: float, activity_level: str) -> float:
    level = activity_level.strip().lower()
    if level not in ACTIVITY_FACTORS:
        raise ValueError(f"activity_level inválido. Use: {list(ACTIVITY_FACTORS.keys())}")
    return bmr * ACTIVITY_FACTORS[level]

def calc_calorie_target(tdee: float, goal_type: str, taxa: str) -> float:
    goal_type = goal_type.strip().lower()
    taxa = taxa.strip().lower()

    if goal_type not in {"emagrecer", "manter", "ganhar_massa"}:
        raise ValueError("goal_type inválido.")
    if taxa not in {"leve", "moderada", "agressiva"}:
        raise ValueError("taxa inválida.")

    if goal_type == "manter":
        return tdee
    if goal_type == "emagrecer":
        mapping = {"leve": -300, "moderada": -450, "agressiva": -600}
        return tdee + mapping[taxa]
    mapping = {"leve": 200, "moderada": 300, "agressiva": 400}
    return tdee + mapping[taxa]

def calc_macros(peso_kg: float, calorias_alvo: float, goal_type: str) -> dict:
    goal_type = goal_type.strip().lower()
    protein_g_per_kg = 2.0 if goal_type == "emagrecer" else 1.8
    fat_g_per_kg = 0.9

    proteina_g = protein_g_per_kg * peso_kg
    gordura_g = fat_g_per_kg * peso_kg

    kcal_from_protein = proteina_g * 4
    kcal_from_fat = gordura_g * 9
    remaining = max(calorias_alvo - (kcal_from_protein + kcal_from_fat), 0)
    carbo_g = remaining / 4

    return {"proteina": round(proteina_g), "gordura": round(gordura_g), "carbo": round(carbo_g)}

def compute_intake(
    sexo: str,
    idade: int,
    altura_cm: float,
    peso_kg: float,
    atividade_nivel: str,
    objetivo_tipo: str,
    objetivo_taxa: str,
) -> Dict[str, Any]:
    bmr = calc_bmr_harris_benedict_revised(sexo, peso_kg, altura_cm, idade)
    tdee = calc_tdee(bmr, atividade_nivel)
    alvo = calc_calorie_target(tdee, objetivo_tipo, objetivo_taxa)
    macros = calc_macros(peso_kg, alvo, objetivo_tipo)

    return {"tmb": bmr, "tdee": tdee, "calorias_alvo": alvo, "macros_g": macros}