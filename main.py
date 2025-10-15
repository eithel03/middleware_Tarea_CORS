from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

app = FastAPI(title="API Middleware CORS - Eithel Herrera")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
def main():
    return "RAIZ API -Metodo GET"

@app.get("/hello/")
def hello():
    return "Este es el API Inicial del ITI-621"

@app.get("/api/personas/")
def getPersonas():
    return {"id":"208490055", "Nombre":"Eithel", "telefono":"84599184" }

@app.get("/api/info/")
def get_info(request: Request):
    data = {
        "autor": "Eithel Herrera",
        "curso": "Tecnologías y Sistemas Web III",
        "estado": "Middleware CORS activo correctamente",
        "cliente": request.client.host
    }
    return JSONResponse(content=data)