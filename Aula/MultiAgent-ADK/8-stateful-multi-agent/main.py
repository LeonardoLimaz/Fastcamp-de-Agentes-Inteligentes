import asyncio

# Import the main customer service agent
from customer_service_agent.agent import customer_service_agent
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from utils import add_user_query_to_history, call_agent_async

load_dotenv()

# ===== PART 1: Initialize In-Memory Session Service =====
# Using in-memory storage for this example (non-persistent)
session_service = InMemorySessionService() # Cria-se uma sessão na memória


# ===== PART 2: Define Initial State =====
# This will be used when creating a new session
initial_state = { # Cria-se o estado inicial
    "user_name": "Brandon Hancock", # Nome do usuário
    "purchased_courses": [], # Lista de cursos que ele já comprou
    "interaction_history": [], # Histórioco de interações
}


async def main_async():
    # Setup constants
    APP_NAME = "Customer Support"
    USER_ID = "aiwithbrandon"

    # ===== PART 3: Session Creation =====
    # Create a new session with initial state
    new_session = session_service.create_session( # Cria-se uma nova sessão
        app_name=APP_NAME, # Essa sessão nova faz parte do APP_NAME
        user_id=USER_ID, # Essa conversa pertence ao id do usuário USER_ID
        state=initial_state, # Passa pelo estado inicial
    )
    SESSION_ID = new_session.id
    print(f"Created new session: {SESSION_ID}")

    # ===== PART 4: Agent Runner Setup =====
    # Create a runner with the main customer service agent
    runner = Runner( # Cria-se o runner
        agent=customer_service_agent, # Passa-se o agente
        app_name=APP_NAME,
        session_service=session_service, # Passa-se o serviço de sessão
    )

    # ===== PART 5: Interactive Conversation Loop =====
    # A partir dessa parte é basicamente uma permissão para que os usuários digitem um requisição
    # captura essa requisição e envia para o runner 
    print("\nWelcome to Customer Service Chat!") 
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ") # Usuário fornece sua requisição

        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Goodbye!")
            break

        # Update interaction history with the user's query
        add_user_query_to_history(
            session_service, APP_NAME, USER_ID, SESSION_ID, user_input
        )

        # Process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

    # ===== PART 6: State Examination =====
    # Show final session state
    final_session = session_service.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")


def main():
    """Entry point for the application."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
