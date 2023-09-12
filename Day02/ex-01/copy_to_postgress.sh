docker cp /Users/kvebers/goinfre/subject/customer/data_2022_dec.csv postgres:/tmp/data_2022_dec.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2022_nov.csv postgres:/tmp/data_2022_nov.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2022_oct.csv postgres:/tmp/data_2022_oct.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2023_jan.csv postgres:/tmp/data_2023_jan.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2023_feb.csv postgres:/tmp/data_2023_feb.csv
docker cp /Users/kvebers/goinfre/subject/item/item.csv postgres:/tmp/item.csv

python3.10 table.py