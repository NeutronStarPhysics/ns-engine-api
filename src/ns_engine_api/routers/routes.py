from fastapi import APIRouter, status, Depends
from ..domain.request import ExecutionRequest
import logging
from ..router import route_request

logger = logging.getLogger(__name__)

api_router = APIRouter()

@api_router.get("/live")
async def main_live():
  return {"OK"}

@api_router.post("/execute", status_code=status.HTTP_201_CREATED)
@api_router.post("/execute/", status_code=status.HTTP_201_CREATED)
async def execute_request(executionRequest: ExecutionRequest):
  try:
    request = ExecutionRequest(**executionRequest.model_dump())
    logger.info("### execute_request: " + str(request))
    return route_request(request)
  except Exception as exception:
    logger.error("execute_request: " + str(exception))

