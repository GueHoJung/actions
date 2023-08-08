#!/bin/sh
echo "PDI : $$, START TIME : $(date +%Y)-$(date +%M)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)"
echo "CD - Linux  Perform : Docker Hub Pull Process"
echo "CI - Github Perform : Actions Script"


attempt=0
isFlagFound=0
while [ $isFlagFound -eq 0 ]
do
	sleep 3
	echo "PDI : $$, CHECK TIME : $(date +%Y)-$(date +%M)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)"
	echo "Attempt To Find Flag ${attempt} Times"
	attempt=$(expr $attempt + 1)
if [ -f "./flag" ]
then
	echo "Flag Is Exist!"
	echo "Docker Hub Pull Process Is Now Performed"
#	docker compose -f ../docker-compose.dev.yml down -v
#	docker compose -f ../docker-compose.dev.yml up --build
	isFlagFound=1
else
	echo "Flag Is Not Exist!"
fi

done

echo "Docker Hub Pull Process Is Stopped"
echo "PDI : $$, END TIME : $(date +%Y)-$(date +%M)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)"

