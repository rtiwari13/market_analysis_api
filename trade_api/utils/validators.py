from fastapi import HTTPException

def validate_sector(sector: str):
    valid_sectors = {"pharmaceuticals", "technology", "agriculture", "finance", "energy"}
    if sector.lower() not in valid_sectors:
        raise HTTPException(status_code=400, detail=f"Invalid sector: {sector}")
