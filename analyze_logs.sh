#!/bin/bash

echo "Отчет о логе веб-сервера" > report.txt
echo "========================" >> report.txt

queryCount=0
while IFS= read -r line; do
	if [[ $line =~ (GET|POST|PUT|DELETE|PATCH) ]]; then
		let queryCount+=1
	fi
done < access.log
echo -e "Общее количество запросов:\t"$queryCount >> report.txt

echo -e "Количество уникальных IP-адресов:\t"$(awk '{print $1}' access.log | sort -u | wc -l) >> report.txt

echo -e "\nКоличество запросов по методам:" >> report.txt
awk '{print $6}' access.log | sort | uniq -c | sed 's/"//' >> report.txt

echo -e "\nСамый популярный URL:\t"$(awk '{print $7}' access.log | sed 's|/||' |sort | uniq -c | sort -r | head -1) >> report.txt

echo "Отчет сохранен в файл report.txt"
