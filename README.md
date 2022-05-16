# Как запустить backend

1) Создать виртуальное окружение `python3 -m venv venv`
2) Активировать виртуальное окружение `source venv/bin/activate` (Linux) `venv/scripts/activate.bat` (Windows)
3) Скачать репозиторий
4) Установить зависимости `pip3 install -r requirements.txt`
5) Запустить сервер `python3 manage.py runserver`

# Куда отправлять pdf

PDF отправлять на точку доступа `api/v1/upload` в формате `base64` в атрибуте `file`.

Результат вернется в формате `base64` как картинка в атрибуте `base64img`.

Сконвертировать PDF в `base64` на ReactJS можно так:
https://stackoverflow.com/questions/49795303/encode-pdf-to-base64-in-reactjs

# Куда отправлять картинку для предсказания

Картинку отправлять на точку доступа `api/v1/predict` в формате `base64` в атрибуте `image`.

Результат вернется в формате `json`. Предсказание будет доступно по атрибуту `prediction`. 

При ошибке вернется `json` с ошибкой, текст которой будет доступен по атрибуту `error`.

# Как развернуть бэкенд в Docker-контейнере

1. Находясь в директории с репозиторием, собрать образ: `docker build -t cardiohelper .`.
2. Создать контейнер с именем `cardiohelper` и запустить в фоне:  `docker run -p 8000:8000 --name cardiohelper -d cardiohelper`.
3. Остановить контейнер: `docker stop cardiohelper`.
4. Повторно запустить уже созданный контейнер: `docker stop cardiohelper`.

# Как протестировать точки доступа

cURL: 

`(echo -n '{"file": "'; base64 file.pdf; echo '"}') | curl -H "Content-Type: application/json" -d @-  http://127.0.0.1:8000/api/v1/upload`

`(echo -n '{"image": "'; base64 ecg.jpg; echo '"}') | curl -H "Content-Type: application/json" -d @-  http://127.0.0.1:8000/api/v1/predict `

