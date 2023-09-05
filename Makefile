start:
	docker-compose -f docker-compose.yml up -d
stop:
	docker-compose -f docker-compose.yml down
j:
	docker exec -it postgres bash

.PHONY: up down connect
