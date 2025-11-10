import os
from dotenv import load_dotenv
from fastapi import FastAPI, Body
import keyboard
import time
import uvicorn

app = FastAPI()


@app.post("/press")
def press_key(input: dict = Body(...)):
    """Press and release a key immediately"""
    duration_seconds: float = input.get("duration_seconds", 0.1)
    key: str = input.get("key", "")

    try:
        keyboard.press(key)
        time.sleep(duration_seconds)
        keyboard.release(key)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "success", "action": "press", "key": key, "duration_seconds": duration_seconds}


@app.post("/hold")
def hold_key(input: dict = Body(...)):
    """Hold down a key for an extended period by repeating"""
    key: str = input.get("key", "")

    try:
        keyboard.press(key)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {
        "status": "success",
        "action": "hold",
        "key": key,
    }


@app.post("/release")
def release_key(input: dict = Body(...)):
    """Release a held key"""
    key: str = input.get("key", "")

    try:
        keyboard.release(key)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "success", "action": "release", "key": key}


@app.get("/")
def read_root():
    return {"message": "Keyboard Input Server is running"}


if __name__ == "__main__":
    load_dotenv()

    HOST: str = os.getenv("HOST", "")
    PORT: int = int(os.getenv("PORT", ""))

    uvicorn.run(app, host=HOST, port=PORT)
