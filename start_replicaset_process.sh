sudo mongod --replSet m101 --logpath "1111.log" --dbpath /data/rs1 --port 27017 --smallfiles --oplogSize 64 --fork

sudo mongod --replSet m101 --logpath "222.log" --dbpath /data/rs2 --port 27018 --smallfiles --oplogSize 64 --fork

sudo mongod --replSet m101 --logpath "333.log" --dbpath /data/rs3 --port 27019 --smallfiles --oplogSize 64 --fork


