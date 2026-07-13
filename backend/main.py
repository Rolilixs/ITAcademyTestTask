import fastapi
from .wallets import api


app = fastapi.FastAPI(title="ITAcademy Test Task API")
app.include_router(api.router)


@app.get("/")
def root():
    return {"text": "Тут пусто. Че нада?"}
