# Дипломный проект. Задание 3: UI тесты

Проект автоматизации UI тестов для сервиса Stellar Burgers: https://stellarburgers.nomoreparties.site/

Описаны элементы, которые используются в тестах, с помощью паттерна Page Object Model.

Протестирована функциональность в Google Chrome и Mozilla Firefox.

## Проведены тесты:

### 1. Восстановление пароля:
- переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
- ввод почты и клик по кнопке «Восстановить»,
- клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
- 
### 2. Личный кабинет:
- переход по клику на «Личный кабинет»,
- переход в раздел «История заказов»,
- выход из аккаунта.
- 
### 3. Проверка основного функционала:
- переход по клику на «Конструктор»,
- переход по клику на «Лента заказов»,
- если кликнуть на ингредиент, появится всплывающее окно с деталями,
- всплывающее окно закрывается кликом по крестику,
- при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
- залогиненный пользователь может оформить заказ.
- 
### 4. Раздел «Лента заказов»:
- если кликнуть на заказ, откроется всплывающее окно с деталями,
- заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
- при создании нового заказа счётчик Выполнено за всё время увеличивается,
- при создании нового заказа счётчик Выполнено за сегодня увеличивается,
- после оформления заказа его номер появляется в разделе В работе.

## Структура проекта
- `tests` - пакет, содержащий тесты
- `pages` - пакет, содержащий методы по взаимодействию с элементами на веб страницах
- `locators` - пакект, содержащий локаторы элементов на веб страницах
- `allure_results` - пакет, содержащий локаторы отчёта тестирования в Allure
- `data.py` - файл содержащий необходимые данные для работы тестов, такие как разрещение экрана, URL, данные тестового пользователя
- `requirements.txt` - текстовый документ содержащий список необходимых библиотек для запусков автотестов

## Запуск автотестов

1. Установка зависимостей

> `pip install -r requirements.txt`

2. Запуск автотестов и составление отчётов в Allure

> `pytest tests --alluredir=allure_results\`

3. Оформление отчёта в веб интерфейче Allure

> `allure serve allure_results`
