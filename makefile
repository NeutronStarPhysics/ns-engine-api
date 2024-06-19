.DEFAULT_GOAL := help
.PHONY: all build run


help:
	@echo 'Available commands:'
	@echo -e 'run \t\t - \t Executes script'

run: 
	uvicorn --app-dir ./src/ --log-config=./src/ns_engine_api/log_conf.yaml ns_engine_api.main:app

runr: 
	uvicorn --reload --app-dir ./src/ --log-config=./src/ns_engine_api/log_conf.yaml ns_engine_api.main:app

st: 
	./tests/smoketest.sh

actuatorui:
	docker run --rm --name spring-boot-admin -p 8080:8080 michayaak/spring-boot-admin:2.2.3-1

