from google.adk.agents import LlmAgent
from root_agent.sub_agents.diet_agent.tools import build_diet_plan

MODEL = "gemini-2.5-flash"

diet_agent = LlmAgent(
    name="diet_agent",
    model=MODEL,
    output_key="diet",
    tools=[build_diet_plan],
    instruction="""
Você recebe em state["intake"] um JSON (pode ser dict ou string JSON).
Extraia:
- dieta_tipo = intake.profile.restricoes.dieta
- refeicoes_dia = intake.profile.rotina.refeicoes_dia
- calorias_alvo = intake.calculos.calorias_alvo
- proteina_g/gordura_g/carbo_g = intake.calculos.macros_g

Chame build_diet_plan com esses campos.
Saída FINAL: APENAS JSON válido: {"dieta": <saida_da_tool>}
""",
)