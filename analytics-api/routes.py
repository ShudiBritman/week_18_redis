from fastapi import APIRouter




router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)



@router.get("/alerts-by-border-and-priority")
def get_border_distribution():
    pass


@router.get("/top-urgent-zones")
def get_top_5_area():
    pass


@router.get("/distance-distribution")
def get_distance_distribution():
    pass

router.get("/low-visibility-high-activity")
def get_dangerous_area():
    pass


router.get("/hot-zones")
def get_close_and_urgent_alerts():
    pass