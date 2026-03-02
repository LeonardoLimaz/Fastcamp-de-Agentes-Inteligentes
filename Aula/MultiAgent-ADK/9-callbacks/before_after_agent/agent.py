"""
Before and After Agent Callbacks Example

This example demonstrates how to use both before_agent_callback and after_agent_callback 
for logging purposes.
"""

from datetime import datetime
from typing import Optional

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types


def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]: # É preciso passar callback context e o retorno será uma mensagem opcional (sem não tiver a mensagem é None)
    """
    Simple callback that logs when the agent starts processing a request.

    Args:
        callback_context: Contains state and context information

    Returns:
        None to continue with normal agent processing
    """
    # Get the session state
    state = callback_context.state # Passando o estado da sessão

    # Record timestamp
    timestamp = datetime.now()

    # Set agent name if not present
    if "agent_name" not in state: # Verifica se tem agent_name
        state["agent_name"] = "SimpleChatBot"

    # Initialize request counter
    if "request_counter" not in state: # Verifica se o pedido já existe no estado
        state["request_counter"] = 1 # Se não existir, define como um pedido
    else:
        state["request_counter"] += 1 # Se existir, adiciona mais um pedido ao número de pedidos

    # Store start time for duration calculation in after_agent_callback
    state["request_start_time"] = timestamp # Armazena o tempo de início do pedido

    # Log the request
    print("=== AGENT EXECUTION STARTED ===")
    print(f"Request #: {state['request_counter']}")
    print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    # Print to console
    print(f"\n[BEFORE CALLBACK] Agent processing request #{state['request_counter']}")

    return None


def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]: # É preciso passar callback context e o retorno será uma mensagem opcional (sem não tiver a mensagem é None)
    """
    Simple callback that logs when the agent finishes processing a request.

    Args:
        callback_context: Contains state and context information

    Returns:
        None to continue with normal agent processing
    """
    # Get the session state
    state = callback_context.state # Passando o estado da sessão

    # Calculate request duration if start time is available
    timestamp = datetime.now() # Pega o tempo atual
    duration = None
    if "request_start_time" in state: # Verifica se o tempo incial do pedido está no estado
        duration = (timestamp - state["request_start_time"]).total_seconds() # Calcula a duração desde o tempo de início do pedido até o tempo de agora

    # Log the completion
    print("=== AGENT EXECUTION COMPLETED ===")
    print(f"Request #: {state.get('request_counter', 'Unknown')}")
    if duration is not None:
        print(f"Duration: {duration:.2f} seconds")

    # Print to console
    print(
        f"[AFTER CALLBACK] Agent completed request #{state.get('request_counter', 'Unknown')}"
    )
    if duration is not None:
        print(f"[AFTER CALLBACK] Processing took {duration:.2f} seconds")

    return None


# Create the Agent
root_agent = LlmAgent(
    name="before_after_agent",
    model="gemini-2.5-flash-lite",
    description="A basic agent that demonstrates before and after agent callbacks",
    instruction="""
    You are a friendly greeting agent. Your name is {agent_name}.
    
    Your job is to:
    - Greet users politely
    - Respond to basic questions
    - Keep your responses friendly and concise
    """,
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
)
