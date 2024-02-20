from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud.url_crud import create_url, get_url_by_short_url, get_url_analytics, get_link_history
from app.utils.qr_code_generator import generate_qr_code

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_url/")
async def create_url_endpoint(original_url: str, custom_alias: str = None, db: Session = Depends(get_db)):
    url_db = create_url(db, original_url, custom_alias)
    short_url = url_db.short_url
    qr_code = generate_qr_code(short_url)
    return {"url_data": url_db, "qr_code": qr_code}

@router.get("/get_url/{short_url}")
async def get_url_endpoint(short_url: str, db: Session = Depends(get_db)):
    url = get_url_by_short_url(db, short_url)
    if url:
        return url
    else:
        raise HTTPException(status_code=404, detail="URL not found")

@router.get("/get_url_analytics/{short_url}")
async def get_url_analytics_endpoint(short_url: str, db: Session = Depends(get_db)):
    analytics_data = get_url_analytics(db, short_url)
    if analytics_data:
        return analytics_data
    else:
        raise HTTPException(status_code=404, detail="URL not found")

@router.get("/get_link_history/{user_id}")
async def get_link_history_endpoint(user_id: int, db: Session = Depends(get_db)):
    link_history = get_link_history(db, user_id)
    return link_history