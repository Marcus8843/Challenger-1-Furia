from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("core/home.html", {"request": request})

@app.get("/matches", response_class=HTMLResponse)
async def get_matches(request: Request):
    return templates.TemplateResponse("core/matches.html", {"request": request})

# WebSocket para simular a torcida
@app.websocket("/ws/fan_chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Torcida diz: {data}")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
