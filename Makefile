help:
	@echo "  clean     removes any unnecessary file"
	@echo "  package   creates a tar.gz file"
	@echo "  deploy    deploys pack on a remote machine, requires arguments user=<user>, host=<ip>, port=<port>, path=<path>"

clean:
	rm -Rf ../mininet-topology.tar.gz mn_topo.egg-info .pytest_cache

package:
	make clean; tar -zcvf mininet-topology.tar.gz --exclude='.git' --exclude='Makefile' --exclude='.venv' --exclude='.pytest_cache' --exclude='mininet-topology.tar.gz' -C .. ./mininet-topology

deploy:
	make package && \
	cat ./mininet-topology.tar.gz | ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $(user)@$(host) -p $(port) \
	"tar -zxvf - -C $(path)"
