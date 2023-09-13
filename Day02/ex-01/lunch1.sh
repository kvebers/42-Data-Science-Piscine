echo "Start"
docker cp /Users/kvebers/goinfre/subject/customer/data_2022_dec.csv postgres:/tmp/data_2022_dec.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2022_nov.csv postgres:/tmp/data_2022_nov.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2022_oct.csv postgres:/tmp/data_2022_oct.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2023_jan.csv postgres:/tmp/data_2023_jan.csv
docker cp /Users/kvebers/goinfre/subject/customer/data_2023_feb.csv postgres:/tmp/data_2023_feb.csv
docker cp /Users/kvebers/goinfre/subject/item/item.csv postgres:/tmp/item.csv
echo "Executed Copy"
python3.10 table.py
echo "Executed Copy to Postgres"
python3.10 table1.py
echo "Executed clearing of data"
echo "Fin"