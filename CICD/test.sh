#!/bin/sh

# 백그라운드 실행 명령어 : nohup ./test.sh &
# 백그라운드 실행 종료 명령어 : ps -ef | grep test.sh | grep -v grep | awk '{print $2}' | xargs kill -9
# 로그 파일 위치 : ./logs/$(date +%Y)-$(date +%m)-$(date +%d).out
# ex) ./logs/2023-08-09.out
# 로그 파일 실시간 확인 : tail -f ./logs/$(date +%Y)-$(date +%m)-$(date +%d).out
# ex) tail -f ./logs/2023-08-09.out

# log_echo 한수 선언, echo를 출력하고 날짜별 로그 파일에 로그를 남김
function log_echo() {
  echo "PDI : $$, $1" | tee -a ./logs/$(date +%Y)-$(date +%m)-$(date +%d).out
}

log_echo "====================CD PROCESS START===================="
log_echo "START TIME : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)"
log_echo "CD - Linux  Perform : Docker Hub Pull Process"
log_echo "CI - Github Perform : Actions Script"


attempt=0
isFlagFound=0
while [ $isFlagFound -eq 0 ]
do
  log_echo "====================FLAG CHECK START===================="
	sleep 60
	log_echo "CHECK TIME : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)"
	log_echo "Attempt To Find Flag ${attempt} Times"
	attempt=$(expr $attempt + 1)
if [ -f "./flag" ]
then
	log_echo "Flag Is Exist!"
	log_echo "Docker Hub Pull Process Is Now Performed"
#	docker compose -f ../docker-compose.dev.yml down -v
#	docker compose -f ../docker-compose.dev.yml up --build
#	isFlagFound=1
  rm -f ./flag
else
	log_echo "Flag Is Not Exist!"
fi
  log_echo "=====================FLAG CHECK END====================="
done

log_echo "Docker Hub Pull Process Is Stopped"
log_echo "END TIME : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)"
log_echo "=====================CD PROCESS END====================="

