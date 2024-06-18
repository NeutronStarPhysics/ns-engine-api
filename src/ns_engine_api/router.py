from fastapi import FastAPI
from .domain.request import ExecutionRequest
from .algorithms.tov_solver.main import TOV_Solver
import logging

logger = logging.getLogger(__name__)

def route_request(request: ExecutionRequest):
    logger.debug(">>> ROUTE_REQUEST: request" + str(request))

    tov_Solver = TOV_Solver()
    tov_Solver.run()
    return request