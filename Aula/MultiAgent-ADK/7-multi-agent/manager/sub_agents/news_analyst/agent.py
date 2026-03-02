from google.adk.agents import Agent
from google.adk.tools import google_search # Importa ferramentas integradas do ADK

news_analyst = Agent(
    name="news_analyst", # Mesmo nome da pasta
    model="gemini-2.5-flash-lite", # Modelo usado no agente
    description="News analyst agent", # Descrição do que ele faz
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    When asked about news, you should use the google_search tool to search for the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    """,
    tools=[google_search],
)
