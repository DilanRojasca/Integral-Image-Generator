from fastapi import APIRouter, HTTPException
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/static", StaticFiles(directory="app/static"), name="static")