from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import mysql.connector

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="test",
        password="Innomatics@123",
        database="product_db"
    )
    return connection


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.get("/products", response_class=HTMLResponse)
def display_products(request: Request):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, price FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": products}
    )
