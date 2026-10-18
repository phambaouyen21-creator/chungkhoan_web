from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Mo phong bien dong gia cua mot ma chung khoan.")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {
        "request":request,
        "ma_co_phieu": "abc-10",
        "thong_tin_sinh_vien":{
            "ho_ten":"Phạm Thị Bảo Uyên",
            "mssv": "3110525043",
            "lop": "25CKDL",
            "truong": "ĐH Sư phạm - Đại học Đà Nẵng"
        }
    }
    return templates.TemplateResponse(
        request=request, name="index.html", context=context
    )
@app.get("/health")
async def health():
    return {"status": "ok"}
