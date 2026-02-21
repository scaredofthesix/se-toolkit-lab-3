"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===

# UNCOMMENT AND FILL IN

@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
) -> list[Learner]:
    """Get all learners."""
    return await read_learners(session, enrolled_after)

# ===
# PART B: POST endpoint
# ===

# UNCOMMENT AND FILL IN
@router.post("/", response_model=Learner, status_code=status.HTTP_201_CREATED)
async def post_learner(
    learner: LearnerCreate,
    session: AsyncSession = Depends(get_session),
) -> Learner:
    """Create a new learner."""
    return await create_learner(session, learner.name, learner.email)

