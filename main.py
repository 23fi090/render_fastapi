from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

app=FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>My Home Page</title>
        </head>
        <body>
            <h1>Hello!!</h1>
            <h2>I'm 23FI090</h2><br>
            <h1>I love eating ramen so much!</h1>
            <div class="loop_wrap">
              <img src="C:/23fi090/images/ramen.jpg"><img src="C:/23fi090/images/ramen.jpg">
            </div><br>
            <h3>contact me<br>
                23fi090@ms.dendai.ac.jp
            </h3>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。{present}ありがとう。今日も暑いですね。水分補給を忘れずに。"}  # f文字列というPythonの機能を使っている