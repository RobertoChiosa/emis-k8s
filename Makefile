.PHONY: git-clean
git-clean:
	@echo "Removing cache"
	git commit -m "Cleaning and removing cache"
	git rm -r --cached .
	git add .

.PHONY: setup
setup:
	@echo "Create env file"
	cp .env-example .env

.PHONY: build
build:
	@echo "Running docker-compose"
	cd services && \
	docker-compose build

.PHONY: run
run:
	@echo "Running docker-compose"
	cd services && \
	docker-compose up -d

.PHONY: stop
stop:
	@echo "Stopping docker-compose"
	cd services && \
	docker-compose down