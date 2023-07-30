from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from src.db.database import db

from . import api

app = FastAPI()
app.include_router(api.api_router, prefix="/api")

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8080/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/wssample")
async def get():
    """
    Args
        test str: テスト
    """
    return HTMLResponse(html)


@app.get("/api/items/{item_id}")
def read_item(item_id: str, q: str = None):
    item = db.find({"item_id": item_id})
    return item


@app.post("/api/items")
def update_items(req: str):
    return db.insert_one(req)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
