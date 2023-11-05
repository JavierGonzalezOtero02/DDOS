﻿#!/bin/bash
echo '##########################################################'
echo 'Address assignation to the different switches interfaces #'
echo '##########################################################'
curl -X POST -d '{"address": "10.1.1.1/24"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"address": "10.10.40.2/30"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"address": "10.10.15.1/30"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"address": "10.1.2.1/24"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"address": "10.10.50.2/30"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"address": "10.10.25.1/30"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"address": "10.1.3.1/24"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"address": "10.10.60.2/30"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"address": "10.10.35.1/30"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"address": "10.1.4.1/24"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"address": "10.10.70.2/30"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"address": "10.10.45.1/30"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"address": "10.10.20.1/30"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"address": "10.10.30.1/30"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"address": "10.10.10.1/29"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"address": "10.10.40.1/30"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"address": "10.10.50.1/30"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"address": "10.10.20.2/30"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"address": "10.10.60.1/30"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"address": "10.10.70.1/30"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"address": "10.10.30.2/30"}' http://localhost:8080/router/000000000000001e
echo
echo '########################################################'
echo 'Routes definition to the different subnets             #'
echo '########################################################'
curl -X POST -d '{"destination": "10.1.2.0/24", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.1.3.0/24", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.1.4.0/24", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.10.0/29", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.20.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.30.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.50.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.60.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.70.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.25.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.35.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.10.45.0/30", "gateway": "10.10.40.1"}' http://localhost:8080/router/0000000000000001
echo
curl -X POST -d '{"destination": "10.1.1.0/24", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.1.3.0/24", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.1.4.0/24", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.10.0/29", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.20.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.30.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.40.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.60.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.70.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.15.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.35.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.10.45.0/30", "gateway": "10.10.50.1"}' http://localhost:8080/router/0000000000000002
echo
curl -X POST -d '{"destination": "10.1.1.0/24", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.1.2.0/24", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.1.4.0/24", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.10.0/29", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.20.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.30.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.40.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.50.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.70.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.15.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.25.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.10.45.0/30", "gateway": "10.10.60.1"}' http://localhost:8080/router/0000000000000003
echo
curl -X POST -d '{"destination": "10.1.1.0/24", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.1.2.0/24", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.1.3.0/24", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.10.0/29", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.20.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.30.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.40.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.50.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.60.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.15.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.25.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.10.35.0/30", "gateway": "10.10.70.1"}' http://localhost:8080/router/0000000000000004
echo
curl -X POST -d '{"destination": "10.1.1.0/24", "gateway": "10.10.20.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.1.2.0/24", "gateway": "10.10.20.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.1.3.0/24", "gateway": "10.10.30.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.1.4.0/24", "gateway": "10.10.30.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.40.0/30", "gateway": "10.10.20.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.50.0/30", "gateway": "10.10.20.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.60.0/30", "gateway": "10.10.30.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.70.0/30", "gateway": "10.10.30.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.15.0/30", "gateway": "10.10.20.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.25.0/30", "gateway": "10.10.20.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.35.0/30", "gateway": "10.10.30.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.10.45.0/30", "gateway": "10.10.30.2"}' http://localhost:8080/router/000000000000000a
echo
curl -X POST -d '{"destination": "10.1.1.0/24", "gateway": "10.10.40.2"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.1.2.0/24", "gateway": "10.10.50.2"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.1.3.0/24", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.1.4.0/24", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.10.0/29", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.30.0/30", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.60.0/30", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.70.0/30", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.15.0/30", "gateway": "10.10.40.2"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.25.0/30", "gateway": "10.10.50.2"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.35.0/30", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.10.45.0/30", "gateway": "10.10.20.1"}' http://localhost:8080/router/0000000000000014
echo
curl -X POST -d '{"destination": "10.1.1.0/24", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.1.2.0/24", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.1.3.0/24", "gateway": "10.10.60.2"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.1.4.0/24", "gateway": "10.10.70.2"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.10.0/29", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.20.0/30", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.40.0/30", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.50.0/30", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.15.0/30", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.25.0/30", "gateway": "10.10.30.1"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.35.0/30", "gateway": "10.10.60.2"}' http://localhost:8080/router/000000000000001e
echo
curl -X POST -d '{"destination": "10.10.45.0/30", "gateway": "10.10.70.2"}' http://localhost:8080/router/000000000000001e
echo
echo '##########################################################'
echo 'Configuration                                            #'
echo '##########################################################'
curl http://localhost:8080/router/all
echo
