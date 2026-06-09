from fastapi import APIRouter, Query
from controllers.probControl import ProbabilityController

router = APIRouter()


@router.get("/probability")
async def get_probability(
    player_cards: str = Query(
        ...
    ),

    comm_cards: str = Query(
        default=""
    ),

    total_players: int = Query(
        ...
    )
):

    result = ProbabilityController(player_cards=player_cards,comm_cards=comm_cards,total_players=total_players).calculate_probability()

    return {
        "success": True,
        "probability": result
    }