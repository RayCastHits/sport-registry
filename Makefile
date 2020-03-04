# Including commands
run-django-server:
	poetry run task server localhost:8000

run-webpack-server:
	yarn serve

open-localhost:
	poetry run python -m webbrowser "http://localhost:8000"

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate


# Primary commands
.PHONY: install
install:
	poetry install --no-root
	yarn
	poetry run task initconfig --debug
	@make migrate

.PHONY: install-prod
install-prod:
	poetry install --no-root
	yarn
	poetry run task initconfig

.PHONY: run
run:
	@make -j 3 run-django-server run-webpack-server open-localhost

.PHONY: build
build:
	yarn build
	poetry run task collectstatic
	@make migrate

.PHONY: deploy
deploy:
	@make build
	sudo systemctl restart gunicorn
	sudo systemctl restart nginx

.PHONY: docker-run
docker-run:
	poetry run task dockervolumes
	docker-compose up
