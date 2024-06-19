import logging
import os
from fastapi import FastAPI, Depends

from .domain.request import ExecutionRequest
from . import actuator
from .dependencies import get_query_token, get_token_header

# from .routers.routes import api_router
from .routers import routes

logger = logging.getLogger(__name__)

app = FastAPI(
    title="NS-ENGINE-API-Server",
    docs_url="/api",
    # dependencies=[Depends(get_query_token)]
)

if os.environ.get('ACTUATOR_ENABLED', 'False') == 'True':
  logger.info("Actuator enabled")
  actuator.setup_actuator(app)
else:
  logger.info("Actuator disabled")


app.include_router(routes.api_router)

@app.get("/")
async def main_route():
  logger.info("main_route")
  return {"message": "ns-engine-api:OK"}

