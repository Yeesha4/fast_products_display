from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Product


app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.get("/products", response_class=HTMLResponse)
def display_products(
    request: Request,
    db: Session = Depends(get_db)
):
    products = db.query(Product).all()

    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": products}
    )
