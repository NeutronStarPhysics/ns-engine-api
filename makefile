.DEFAULT_GOAL := help
.PHONY: all build run


help:
	@echo 'Available commands:'
	@echo -e 'run \t\t - \t Executes script'

run: 
	uvicorn --app-dir ./src/ ns_engine_api.main:app

runr: 
	uvicorn --reload --app-dir ./src/ ns_engine_api.main:app
