from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import json

activities_agent = Agent(
    name="activities_agent", # Nome do agente
    model=LiteLlm("gemini-2.5-flash-lite"), # Modelo de LLM usado pelo agente
    description="Suggests interesting activities for the user at a destination.", # Descrição do que o agente faz
    instruction=( # Instrução do como o agente deve executar sua função
        "Given a destination, dates, and budget, suggest 2-3 engaging tourist or cultural activities. "
        "For each activity, provide a name, a short description, price estimate, and duration in hours. "
        "Respond in plain English. Keep it concise and well-formatted."
    )
)

session_service = InMemorySessionService() # Cria um serviço de sessão em memória
runner = Runner(
    agent=activities_agent, # Define o agente executado pelo runner
    app_name="activities_app", # Define o nome da aplicação que está usando o agente
    session_service=session_service # Informa ao runner qual serviço de sessão ele deve usar para gerenciar o estado das conversas
)
USER_ID = "user_activities" # Define o ID de usuário
SESSION_ID = "session_activities" # Define o ID de sessão

async def execute(request):
    session_service.create_session( # Cria uma nova sessão de conversa
        app_name="activities_app", # Passa o nome da aplicação
        user_id=USER_ID, # Passa o ID do usuário
        session_id=SESSION_ID # Passa o ID da sessãom
    )
    prompt = ( # Criação de um prompt que será enviado para o agente
        f"User is flying to {request['destination']} from {request['start_date']} to {request['end_date']}, "
        f"with a budget of {request['budget']}. Suggest 2-3 activities, each with name, description, price estimate, and duration. "
        f"Respond in JSON format using the key 'activities' with a list of activity objects."
    )
    message = types.Content(role="user", parts=[types.Part(text=prompt)]) # Cria uma mensagem no formato esperado pelo sistema de agentes
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message): # Executa o agente de forma assíncrona usando o runner
        if event.is_final_response(): # Verifica se o evento recebido é a resposta final do agente
            response_text = event.content.parts[0].text # Extrai o texto da resposta do agente
            try:
                parsed = json.loads(response_text) # Converte o texto da resposta em um objeto JSON
                if "activities" in parsed and isinstance(parsed["activities"], list): # Verifica se o JSON possui a chave "activities" e se o valor é uma lista
                    return {"activities": parsed["activities"]} # Retorna a lista de atividades extraída do JSON
                else: # Caso o JSON não esteja no formato esperado
                    print("'activities' key missing or not a list in response JSON")
                    return {"activities": response_text}  # Retorna o texto bruto da resposta como fallback
            except json.JSONDecodeError as e: # Captura erros caso a resposta não seja um JSON válido
                print("JSON parsing failed:", e)
                print("Response content:", response_text)
                return {"activities": response_text}  # fallback to raw text