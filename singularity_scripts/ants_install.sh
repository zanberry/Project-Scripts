# Run this script only if current pwd = ../ThalSR/singularityContainers

curl -s https://raw.githubusercontent.com/NeuroDesk/neurocommand/main/cvmfs/log.txt && export container=ants_2.5.1_20240429 && curl -X GET https://d15yxasja65rk8.cloudfront.net/$container.simg -O

