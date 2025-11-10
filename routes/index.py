from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Keyboard Input API is running"}


@router.get("/favicon.ico")
def favicon():
    return Response(status_code=204)
