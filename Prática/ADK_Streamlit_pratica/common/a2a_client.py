import httpx
async def call_agent(url, payload): 
    async with httpx.AsyncClient() as client: # Cria um cliente HTTP assíncrono
        response = await client.post(url, json=payload, timeout=60.0)  # Envia uma requisição HTTP POST para a url, com os dados payload
        response.raise_for_status() # Verifica se teve algum erro na requisição
        return response.json() # Retorna o resultado da API em formato JSON