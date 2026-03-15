from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

host_agent = Agent(
    name="host_agent", # Nome do agente
    model=LiteLlm("gemini-2.5-flash-lite"), # Modelo de LLM usado pelo agente
    description="Coordinates travel planning by calling flight, stay, and activity agents.", # Descrição do que o agente faz
    instruction="You are the host agent responsible for orchestrating trip planning tasks. " # Instrução do como o agente deve executar sua função
                "You call external agents to gather flights, stays, and activities, then return a final result."
)
session_service = InMemorySessionService() # Cria um serviço de sessão em memória
runner = Runner(
    agent=host_agent, # Define o agente executado pelo runner
    app_name="host_app", # Define o nome da aplicação que está usando o agente
    session_service=session_service # Informa ao runner qual serviço de sessão ele deve usar para gerenciar o estado das conversas
)
USER_ID = "user_host" # Define o ID de usuário
SESSION_ID = "session_host" # Define o ID de sessão

async def execute(request):
    # Ensure session exists
    session_service.create_session( # # Cria uma nova sessão de conversa
        app_name="host_app", # Passa o nome da aplicação
        user_id=USER_ID, # Passa o ID do usuário
        session_id=SESSION_ID # Passa o ID da sessão
    )
    prompt = ( # Criação de um prompt que será enviado para o agente
        f"Plan a trip to {request['destination']} from {request['start_date']} to {request['end_date']} "
        f"within a total budget of {request['budget']}. Call the flights, stays, and activities agents for results."
    )
    message = types.Content(role="user", parts=[types.Part(text=prompt)]) # Cria uma mensagem no formato esperado pelo sistema de agentes
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message): # Executa o runner, que roda o agente principal
        if event.is_final_response(): # Verifica se o evento recebido corresponde à resposta final do agente
            return {"summary": event.content.parts[0].text} # Extrai o texto da resposta final