# start

初期化：  
docker-compose up --build -d

2 回目以降：  
docker-compose up -d

docker コンテナ内へ入る：  
docker exec -it htmx-test bash

サーバー起動：  
python manage.py runserver 0.0.0.0:8000

# end

docker コンテナから抜ける：  
exit  
docker コンテナから抜ける：  
docker-compose down
