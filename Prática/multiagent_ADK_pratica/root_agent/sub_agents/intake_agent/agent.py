from google.adk.agents import LlmAgent
from root_agent.sub_agents.intake_agent.tools import compute_intake

MODEL = "gemini-2.5-flash"

intake_agent = LlmAgent(
    name="intake_agent",
    model=MODEL,
    description="Coleta dados e calcula TMB/TDEE/calorias alvo/macros via Harris-Benedict revisada.",
    output_key="intake",
    tools=[compute_intake],
    instruction="""
Você é um agente de intake para planejamento de dieta/treino.

Tarefa:
1) Coletar dados faltantes do usuário.
2) Montar um objeto profile (JSON) com os campos abaixo.
3) Chamar a tool compute_intake com os campos necessários.
4) Retornar APENAS JSON válido com:
{
  "profile": { ... },
  "calculos": { ... },  // retorno da tool
  "notas": [ ... ]
}

Campos do profile:
{
  "dados": {"sexo":"M|F","idade":int,"altura_cm":float,"peso_kg":float},
  "atividade": {"nivel":"sedentario|leve|moderado|alto|atleta"},
  "objetivo": {"tipo":"emagrecer|manter|ganhar_massa","taxa":"leve|moderada|agressiva"},
  "rotina": {"refeicoes_dia":int,"treinos_semana":int,"min_por_treino":int},
  "restricoes": {"dieta":"onivoro|vegetariano|vegano","alergias":[...],"alimentos_nao_gosta":[...]},
  "saude": {"lesoes":[...],"observacoes":""}
}

Ao chamar compute_intake, passe:
- sexo, idade, altura_cm, peso_kg
- atividade_nivel = profile["atividade"]["nivel"]
- objetivo_tipo = profile["objetivo"]["tipo"]
- objetivo_taxa = profile["objetivo"]["taxa"]

Regras:
- Pergunte objetivamente um item por vez até completar.
- Saída final: somente JSON (sem texto fora do JSON).
""",
)