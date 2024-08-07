from fastapi import APIRouter, HTTPException
from app.services.image_service import create_image

router = APIRouter()

@router.post("/api/generate")
async def api_generate_image(equation: str):
    try:
        image_path = create_image(equation)
        return{"image_url": image_path}
    except Exception as e:  
        raise HTTPException(status_code=400, detail="Failed to generate image") from e
