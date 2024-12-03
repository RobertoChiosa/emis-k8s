.PHONY: help
help: ## Print this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {gsub("\\\\n",sprintf("\n%22c",""), $$2);printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


.PHONY: git-clean
git-clean: ## Clean and remove cache
	@echo "Removing cache"
	git commit -m "Cleaning and removing cache"
	git rm -r --cached .
	git add .

.PHONY: setup
setup: 		## Create env file
	@echo "Create env file"
	cp .env-example services/.env

.PHONY: build
build: 		## Build docker-compose
	@echo "Running docker-compose"
	cd services && \
	docker compose build

.PHONY: up
up: 		## Run docker compose up
	@echo "Running docker compose"
	cd services && \
	docker compose up -d

.PHONY: stop
down: 		## Stop docker-compose
	@echo "Stopping docker compose down"
	cd services && \
	docker compose down