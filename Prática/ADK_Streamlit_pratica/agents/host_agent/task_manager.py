from common.a2a_client import call_agent
FLIGHT_URL = "http://localhost:8001/run"
STAY_URL = "http://localhost:8002/run"
ACTIVITIES_URL = "http://localhost:8003/run"

async def run(payload):
    #Print what the host agent is sending
    print("Incoming payload:", payload)
    flights = await call_agent(FLIGHT_URL, payload) # Chama o agente de voos
    stay = await call_agent(STAY_URL, payload) # Chama o agente de hospedagem
    activities = await call_agent(ACTIVITIES_URL, payload) # Chama o agente de atividades
    # Log outputs
    print("flights:", flights) # Mostra a resposta do agente de voos
    print("stay:", stay) # Mostra a resposta do agente de hospedagem
    print("activities:", activities) # Mostra a resposta do agente de atividades
    # Ensure all are dicts before access
    flights = flights if isinstance(flights, dict) else {} # Se flights for um dicionário, mantém o valor, se não, substitui por um dicionário vazio.
    stay = stay if isinstance(stay, dict) else {}
    activities = activities if isinstance(activities, dict) else {}
    return { # Retorna o dicionário de resposta final
        "flights": flights.get("flights", "No flights returned."),
        "stay": stay.get("stays", "No stay options returned."),
        "activities": activities.get("activities", "No activities found.")
    }