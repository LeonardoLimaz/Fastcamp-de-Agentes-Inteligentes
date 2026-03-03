from google.adk.agents import SequentialAgent

from root_agent.sub_agents.intake_agent.agent import intake_agent
from root_agent.sub_agents.diet_agent.agent import diet_agent
from root_agent.sub_agents.workout_agent.agent import workout_agent
import json

_original_dumps = json.dumps

class _BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return f"<bytes len={len(obj)}>"
        return super().default(obj)

def _safe_dumps(*args, **kwargs):
    if "cls" not in kwargs or kwargs["cls"] is None:
        kwargs["cls"] = _BytesEncoder
    return _original_dumps(*args, **kwargs)

json.dumps = _safe_dumps


root_agent = SequentialAgent(
    name="root_agent",
    description=(
    "Orquestrador de alto nível de um sistema multi-agente especializado "
    "em planejamento físico-nutricional. Implementa um pipeline sequencial "
    "composto por três agentes especializados (intake, dieta e treino), "
    "mantendo estado compartilhado e integridade de dados entre etapas. "
    "Responsável por garantir coerência entre metas metabólicas, distribuição "
    "de macronutrientes e periodização de treino com filosofia low volume."
    ),
    sub_agents=[intake_agent, diet_agent, workout_agent],
)