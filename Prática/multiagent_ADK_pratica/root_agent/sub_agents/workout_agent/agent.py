from google.adk.agents import LlmAgent
from root_agent.sub_agents.workout_agent.tools import build_low_volume_workout

MODEL = "gemini-2.5-flash"

workout_agent = LlmAgent(
    name="workout_agent",
    model=MODEL,
    output_key="workout",
    tools=[build_low_volume_workout],
    instruction="""
Leia state["intake"] (JSON).
Extraia:
- goal_type = intake.profile.objetivo.tipo
- treinos_semana = intake.profile.rotina.treinos_semana
- min_por_treino = intake.profile.rotina.min_por_treino

Chame build_low_volume_workout(goal_type, treinos_semana, min_por_treino)
Saída FINAL: somente JSON válido {"treino": <saida_da_tool>}
""",
)