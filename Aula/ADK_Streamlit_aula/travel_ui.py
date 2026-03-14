import streamlit as st
import requests

st.set_page_config(page_title="ADK-Powered Travel Planner", page_icon="✈️") # Configura a página do Streamlit, definindo o título da aba e o ícone
st.title("🌍 ADK-Powered Travel Planner") # Título principal da aplicação
origin = st.text_input("Where are you flying from?", placeholder="e.g., New York") # Cria um campo de texto onde o usuário informa a cidade de origem
destination = st.text_input("Destination", placeholder="e.g., Paris") # Cria um campo para o usuário informar o destino da viagem
start_date = st.date_input("Start Date") # Cria um seletor de data para a data de início da viagem
end_date = st.date_input("End Date") # Cria um seletor de data para a data de término da viagem
budget = st.number_input("Budget (in USD)", min_value=100, step=50) # Cria um campo numérico para o orçamento da viagem
if st.button("Plan My Trip ✨"): # Cria um botão que inicia o planejamento da viagem
    if not all([origin, destination, start_date, end_date, budget]): # Verifica se todos os campos foram preenchidos
        st.warning("Please fill in all the details.") # Aviso dado caso algum campo esteja vazio
    else: # Se todos os campos estiverem preenchidos
        payload = {
            "origin": origin,
            "destination": destination,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "budget": budget
        }
        response = requests.post("http://localhost:8000/run", json=payload) # Envia uma requisição POST para a API local (/run), enviando o payload
        if response.ok: # Verifica se a requisição foi bem-sucedida
            data = response.json() # Converte a resposta da API para formato JSON
            st.subheader("✈️ Flights") # Subtítulo para voos
            st.markdown(data["flights"]) # Exibe as opções de voos retornadas pela API
            st.subheader("🏨 Stays") # Subtítulo para hospedagens
            st.markdown(data["stay"]) # Exibe as opções de hospedagens retornadas pela API
            st.subheader("🗺️ Activities") # Subtítulo para atividades
            st.markdown(data["activities"]) # Exibe as opções de atividades retornadas pela API 
        else: # Caso a requisição à API falhe
            st.error("Failed to fetch travel plan. Please try again.")