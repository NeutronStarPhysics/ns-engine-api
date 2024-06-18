from fastapi import FastAPI, status
from .domain.request import ExecutionRequest
from . import router
import logging


# get root logger
logger = logging.getLogger(__name__)

app = FastAPI()   

@app.get("/") 
async def main_route():
  logger.info("main_route")
  return {"message": "ns-engine-api:OK"}

@app.post("/execute", status_code=status.HTTP_201_CREATED)
@app.post("/execute/", status_code=status.HTTP_201_CREATED)
async def execute_request(executionRequest: ExecutionRequest):
  
  try:
    request = ExecutionRequest(**executionRequest.model_dump())
    logger.info("execute_request: " + str(request))
    return router.route_request(request)
  except Exception as exception:
    logger.error("execute_request: " + str(exception))

