import fastapi
from backend.wallets import api


app = fastapi.FastAPI(title="ITAcademy Test Task API")
app.include_router(api.router, prefix="/api/v1", tags=["WALLET"])


@app.get("/")
def root():
    return {"text": "Тут пусто. Че нада? http://127.0.0.1:8000/docs"}
