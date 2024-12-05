from fastapi import APIRouter

router = APIRouter(tags=["Healthcheck"])


@router.get("/v1/healthcheck")
def healthcheck():
    return {"message": "Hello. Server is up and running..."}
