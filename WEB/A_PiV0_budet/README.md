### Структура проекта
Структура директорий проекта:
```sh
.
├── app.py
├── drinks.json
├── static
│   ├── api.js
│   ├── styles.css
│   └── tequila-bottle.png
└── templates
    └── index.html
```

### ToDo
1. Запихать всё в Docker

### How to run
```
git clone https://github.com/cherepawwka/tqlCTF.git
cd tqlCTF
docker build . -t tqlctf
docker run -d -p 80:80 tqlctf:latest
```

To stop container
```
docker ps -a  # get ID
docker stop ID
```
