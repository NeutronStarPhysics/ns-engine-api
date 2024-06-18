import logging
from ...domain.algorithm import Algorithm

logger = logging.getLogger(__name__)

class TOV_Solver(Algorithm):
    def run(self):
        logger.debug(">>> TOV_Solver.run: " + type(self).__name__)
