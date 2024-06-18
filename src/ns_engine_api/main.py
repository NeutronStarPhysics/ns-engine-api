from fastapi import FastAPI
from .domain.request import Request
from . import router

app = FastAPI()   

@app.get("/") 
async def main_route():     
  return {"message": "ns-engine-api:OK"}

@app.post("/execute")
@app.post("/execute/")
async def execute_request(request: Request):
  try:
    return router.route_request(request)
  except Exception as exception:
    print(exception)

