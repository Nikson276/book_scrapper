ТЗ:
1) создать скрипт, который выполняет следующие шаги:
2) Переходит на сайт - https://baza-knig.ink/
3) Переходит по классу short-title, нажимает на ссылку href и переходит к книге 

4)Перешел на страницу книги. Ищет class=tabs, и кликает по блоку


5) Затем ищет class=create_archive, и кликает по нему

6)Открылось окно. Ищет class=ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only. Кликает на этот блок 

7) Открыло окно для скачивания. Ищет блок class = ui-dialog-content ui-widget-content. 

Кликает по href и скачает файл 
8) Все файлы сохранять в отдельную папку с контентом

Реализовано: 
Получение ссылки для первой записи работает.
>>>
User@DESKTOP-PDJ1254 MINGW64 /c/Projects/book_scrapper
$ python main.py

DevTools listening on ws://127.0.0.1:59221/devtools/browser/2f0f7a54-a75f-4059-8438-6ee0420d4bbc
Ссылка получена: https://3s.abooka.casa/z/34648a0f06f5654b74dc8d72344ce540/1696968578/83414_1.zip
<<<

Но скачать по ней из отдельного вызова по этой ссылке нельзя, т.к. на сервере защита по токенам есть.
Каждый сеанс на странице токенизируется (hittoken) и используется при старте скачки по ссылке.

Код сырой, не оптимальный. Это draft для проверки возможностей selenium.