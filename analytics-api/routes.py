from fastapi import APIRouter
from dal import Queri




router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)



@router.get("/alerts-by-border-and-priority")
def get_border_distribution():
    try:
        return Queri.border_distribution()
    except Exception as e:
        return {e}


@router.get("/top-urgent-zones")
def get_top_5_area():
    try:
        return Queri.top_5_area()
    except Exception as e:
        return {e}


@router.get("/distance-distribution")
def get_distance_distribution():
    try:
        return Queri.distance_distribution()
    except Exception as e:
        return {e}

router.get("/low-visibility-high-activity")
def get_dangerous_area():
    try:
        return Queri.dangerous_area()
    except Exception as e:
        return {e}


router.get("/hot-zones")
def get_close_and_urgent_alerts():
    try:
        return Queri.close_and_urgent_alerts()
    except Exception as e:
        return {e}