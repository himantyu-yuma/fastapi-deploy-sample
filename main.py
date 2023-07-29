from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from chat import completion
from database import Database

app = FastAPI()
db = Database("Items", "")


class CreateItemRequest(BaseModel):
    name: str


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
            var ws = new WebSocket("wss://fastapisample-1-b3690512.deta.app/ws");
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


@app.get("/api/ping")
def read_root():
    return {"Hello": "World"}


@app.get("/api/items/{item_name}")
def read_item(item_name: str, q: str = None):
    item = db.find({"name": item_name})[0]
    return item


@app.get("/api/items")
def read_all_items():
    items = db.find({})
    return {"data": items}


@app.post("/api/items")
def update_items(req: CreateItemRequest):
    print(req)
    return db.insert_one({"name": req.name})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


class CreateChatRequest(BaseModel):
    prompt: str


@app.post("/api/chat")
def create_chat(req: CreateChatRequest):
    return completion(req.prompt)
