from fastapi import APIRouter, HTTPException
from app.controllers.generator_controller import generate_image

router = APIRouter()

@router.post("/generate")
async def generate_image_route(equation:str):
    try:
        image_path = generate_image(equation)
        return {"image_url": image_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to generate image")