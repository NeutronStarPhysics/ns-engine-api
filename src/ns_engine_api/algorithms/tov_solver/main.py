import logging
from ...domain.algorithm import Algorithm

logger = logging.getLogger(__name__)

def run(parameters):
    tov_Solver = TOV_Solver()
    tov_Solver.run()

class TOV_Solver(Algorithm):
    def run(self):
        logger.debug(">>> TOV_Solver.run: " + type(self).__name__)
