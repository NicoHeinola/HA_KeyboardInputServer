from fastapi import APIRouter, Body
import keyboard
import time

from middleware.auth import require_auth

router: APIRouter = APIRouter()


@router.post("/press")
def press_key(token: str = require_auth(), input: dict = Body(...)):
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


@router.post("/hold")
def hold_key(token: str = require_auth(), input: dict = Body(...)):
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


@router.post("/release")
def release_key(token: str = require_auth(), input: dict = Body(...)):
    """Release a held key"""
    key: str = input.get("key", "")

    try:
        keyboard.release(key)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "success", "action": "release", "key": key}
