from pydantic import BaseModel


class TravelRequest(BaseModel):
    destination: str # Destino é definido como string
    start_date: str # Data de início é definido como string
    end_date: str # Data de fim é definido como string
    budget: float # Valor da viagem é definido como float
    observations: str = "" # Preferências e restrições adicionais do usuário
