from fastapi import FastAPI
import uvicorn
def create_app(agent):
    app = FastAPI() # Cria uma instância da aplicação FastAPI
    @app.post("/run") # Define uma rota HTTP POST no endpoint /run
    async def run(payload: dict):
        return await agent.execute(payload) # Chama o método execute do agent, passando o payload
    return app # Retorna a aplicação FastAPI criada