# start

初期化：<br>
docker-compose up --build -d<br>

2 回目以降：<br>
docker-compose up -d<br>

docker コンテナ内へ入る：<br>
docker exec -it htmx-test bash<br>

サーバー起動：<br>
python manage.py runserver 0.0.0.0:8000<br>
[http://localhost:8000/](http://localhost:8000/)<br>

# end

docker コンテナから抜ける：<br>
exit<br>

docker コンテナから抜ける：<br>
docker-compose down<br>
