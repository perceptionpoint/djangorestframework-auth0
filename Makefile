init-nexus:
	poetry config repositories.nexus "https://nexus.perception-point.io/repository/pypi-hosted/" &&\
	poetry config http-basic.nexus admin ${NEXUS_PASSWORD}

build:
	poetry build

publish:
	poetry publish -r nexus