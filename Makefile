db:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running db in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose up -d db

dbrestore-dev:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Restore dump from backups/latest.dmp in development mode"
	@echo "------------------------------------------------------------------"
	@echo "------------------------------------------------------------------"
	@# - prefix causes command to continue even if it fails
	@echo "stopping uwsgi container"
	@docker-compose stop web
	@echo "dropping django_geoloc_dev"
	@docker-compose exec -e DATABASE_NAME db bash -c 'su - postgres -c "dropdb django_geoloc_dev"'
	@source .env.dev; echo "creating django_geoloc_dev"
	@docker-compose exec -e DATABASE_NAME db bash -c 'su - postgres -c "createdb -O django_geoloc -T template_postgis django_geoloc_dev"'
	@source .env.dev; echo "restoring django_geoloc_dev"
	@docker-compose exec -e DATABASE_NAME db bash -c 'pg_restore /backups/latest.dmp | su - postgres -c "psql django_geoloc_dev"'
	@docker-compose start web
	@echo "starting uwsgi container"