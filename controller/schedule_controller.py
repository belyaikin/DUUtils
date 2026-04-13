from fastapi import APIRouter

from service import schedule_service

router = APIRouter()


@router.get("/schedules/{group}")
def get_schedule(group: str):
    return schedule_service.get_schedule(group)
