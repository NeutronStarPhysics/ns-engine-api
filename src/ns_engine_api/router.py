from fastapi import FastAPI
from .domain.request import Request

def route_request(request: Request):
    print("request" + str(request))
    return request