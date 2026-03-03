def build_low_volume_workout(goal_type: str, treinos_semana: int, min_por_treino: int) -> dict:
    days = int(treinos_semana)
    mins = int(min_por_treino)

    if days <= 3:
        semana = [
            {"dia": "A (Full Body)", "exercicios": [
                "Agachamento/Leg Press — 2-3x6-10 (RIR 1-3)",
                "Supino — 2-3x6-10 (RIR 1-3)",
                "Remada — 2-3x8-12 (RIR 1-3)",
                "Elevação lateral — 1-2x12-20 (RIR 0-2)",
            ]},
            {"dia": "B (Full Body)", "exercicios": [
                "RDL/Terra — 2-3x5-8 (RIR 1-3)",
                "Desenvolvimento — 2-3x6-10 (RIR 1-3)",
                "Puxada/Barra — 2-3x6-12 (RIR 1-3)",
                "Panturrilha — 1-2x8-15 (RIR 0-2)",
            ]},
            {"dia": "C (Full Body)", "exercicios": [
                "Hack/Agacho frontal — 2-3x6-10 (RIR 1-3)",
                "Supino inclinado — 2-3x6-10 (RIR 1-3)",
                "Remada unilateral — 2-3x8-12 (RIR 1-3)",
                "Tríceps OU bíceps — 1-2x8-15 (RIR 0-2)",
            ]},
        ]
    else:
        semana = [
            {"dia": "Upper 1", "exercicios": [
                "Supino — 2-3x6-10 (RIR 1-3)",
                "Remada — 2-3x8-12 (RIR 1-3)",
                "Desenvolvimento — 1-2x6-10 (RIR 1-3)",
                "Puxada — 1-2x8-12 (RIR 1-3)",
            ]},
            {"dia": "Lower 1", "exercicios": [
                "Agachamento/Leg Press — 2-3x6-10 (RIR 1-3)",
                "Posterior (RDL/Mesa) — 2-3x6-12 (RIR 1-3)",
                "Panturrilha — 1-2x8-15 (RIR 0-2)",
            ]},
            {"dia": "Upper 2", "exercicios": [
                "Supino inclinado — 2-3x6-10 (RIR 1-3)",
                "Puxada/Barra — 2-3x6-12 (RIR 1-3)",
                "Elevação lateral — 1-2x12-20 (RIR 0-2)",
                "Remada (variação) — 1-2x8-12 (RIR 1-3)",
            ]},
            {"dia": "Lower 2", "exercicios": [
                "Agachamento (variação) — 2-3x6-10 (RIR 1-3)",
                "Posterior — 2-3x6-12 (RIR 1-3)",
                "Abdômen — 1-2x10-20",
            ]},
        ]

    if goal_type == "emagrecer":
        cardio = {"frequencia": "3-5x/semana", "duracao": "20-40 min", "tipo": "LISS + opcional 1 HIIT curto"}
    elif goal_type == "ganhar_massa":
        cardio = {"frequencia": "1-3x/semana", "duracao": "10-25 min", "tipo": "leve"}
    else:
        cardio = {"frequencia": "2-3x/semana", "duracao": "15-30 min", "tipo": "leve/moderado"}

    return {"resumo": f"Low volume {days}x/semana (~{mins} min).", "semana": semana[:days], "cardio": cardio}