help:
	@echo "  clean     removes any unnecessary file"
	@echo "  package   creates a tar.gz file"
	@echo "  deploy    deploys pack on a remote machine, requires arguments user=<user>, host=<ip>, port=<port>, path=<path>"
	@echo "  documentation	render documentation"

clean:
	rm -Rf mininet-topology-yaml.tar.gz mininet_topology_yaml.egg-info .pytest_cache dist build sdist

package:
	make clean; tar -zcvf mininet-topology-yaml.tar.gz --exclude='.*' --exclude='Makefile' --exclude='mininet-topology-yaml.tar.gz' -C .. ./mininet-topology-yaml

deploy:
	make package && \
	cat ./mininet-topology-yaml.tar.gz | ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $(user)@$(host) -p $(port) \
	"tar -zxvf - -C $(path)"
	make clean;

documentation:
	cd docs && make html

