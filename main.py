"""from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(req:Request):
    sai_hi = "Hello, Welcome to my cafe"
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )
    
@app.post("/login")
def login(req:Request,username:str = Form(),password:str = Form()):
    print(username,password)
    products = [(1,"Laptop",70000),(2,"iPhone",87000)]
    return templates.TemplateResponse(
        request=req,
        name="product.html",
        context={"products":products}
    )"""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(req:Request):
    sai_hi = "Hello, Welcome to my cafe"
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )

@app.get("/products",response_class=HTMLResponse)
def products(req:Request):
    products = [(1,"Laptop",70000),(2,"iPhone",87000)]
    return templates.TemplateResponse(
        request=req,
        name="product.html",
        context={"products":products}
    )
    
@app.post("/login")
def login(req:Request,username:str = Form(),password:str = Form()):
    print(username,password)
    products = [(1,"Laptop",70000),(2,"iPhone",87000)]
    return templates.TemplateResponse(
        request=req,
        name="product.html",
        context={"products":products}
    )