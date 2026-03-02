from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_current_time

root_agent = Agent(
    name="manager", # Mesmo nome da pasta
    model="gemini-2.5-flash-lite", # Define o modelo que será usado
    description="Manager agent", # Descrição do propósito do agente
    instruction=""" 
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """, # Instrução do que o agente deve fazer e quais funções estão disponíveis para ele
    sub_agents=[stock_analyst, funny_nerd], # Lista dos subagentes disponíveis, subagentes estes que estão criados na pasta dos subagentes
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ], # Lista das ferramentas disponíveis, usando o 'AgentTool' porque "news_analyst" implementa uma ferramenta integrada
)
