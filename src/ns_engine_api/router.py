import logging
from fastapi import FastAPI

from .domain.request import ExecutionRequest
from .algorithms.tov_solver import main as tov_solver

logger = logging.getLogger(__name__)

def route_request(request: ExecutionRequest):
    logger.debug(">>> ROUTE_REQUEST: request" + str(request))

    tov_solver.run(None)
    return request