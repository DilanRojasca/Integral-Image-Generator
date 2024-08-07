# app/main.py
from fastapi import FastAPI
from app.views.home_router import router as home_router
from app.views.generate_image_router import router as generate_image_router
from app.views.static_router import router as static_router
from app.views.api_router import router as api_router

app = FastAPI()

# Incluir los routers sin la barra inclinada al final del prefijo
app.include_router(home_router, prefix="")
app.include_router(generate_image_router, prefix="/generate")
app.include_router(static_router)
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Integral Image Generator"}
