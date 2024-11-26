import logging
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


API_KEY = "8e20087c6d1fa3d1ffa71e3592d93e54"
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info("Página inicial acessada")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    logger.info(f"Solicitação de previsão do tempo para a cidade: {city}")
    try:
        geocode_paramers = {
            "q": city,
            "appid": API_KEY,
            "limit": 1
        }

        geocode_response = request.get(GEOCODE_URL, params=geocode_paramers)
        geocode_response.raise_for_status()
        geocode_data = geocode_response.json()
        
        if not geocode_data:
            logger.warning(f"Cidade '{city}' não encontrada.")
            return templates.TemplateResponse(
                "error.html",
                
            )
        
        # Extração de dados relevantes para exibição

        # Passar dados relevantes para o template
        return templates.TemplateResponse(
            "weather.html",
            {"request": request, "city_name": city, "weather": weather} # não está definida pois temos que fazer o exercício
        )

    except requests.RequestException as e:
        logger.error(f"Erro ao fazer requisição às APIs: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": "Erro ao obter dados do tempo. Por favor, tente novamente."}
        )

    except KeyError as e:
        logger.error(f"Erro ao processar dados das APIs: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": "Erro ao processar dados do tempo. Por favor, tente novamente."}
        )

    except Exception as e:
        logger.exception(f"Erro inesperado: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": "Ocorreu um erro inesperado. Por favor, tente novamente mais tarde."}
        )



# COMANDO PARA SUBIR O SERVIDOR
# uvicorn main:app --reload