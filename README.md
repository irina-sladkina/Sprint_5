# Sprint_5

Автотесты на Selenium для сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/) — учебного приложения, где можно собрать и заказать космический бургер.

## Стек
- Python 3
- pytest
- Selenium WebDriver (Google Chrome)

## Структура проекта
- `tests/` — тесты, сгруппированные по функциональности.
- `conftest.py` — фикстуры: запуск и закрытие браузера, регистрация пользователя, вход в аккаунт.
- `locators.py` — локаторы элементов страниц с комментариями.
- `helpers.py` — генераторы email (логина) и пароля.
- `urls.py` — адреса страниц.
- `data.py` — тестовые данные.

## Запуск
```
pip install -r requirements.txt
pytest -v
```

## Реализованные тесты

### Регистрация (`tests/test_registration.py`)
- `test_registration_valid_data_redirect_to_login_page` — успешная регистрация с корректными данными.
- `test_registration_short_password_error_shown` — ошибка «Некорректный пароль» при пароле короче 6 символов (параметризованный).

### Вход (`tests/test_login.py`)
- `test_login_from_different_entry_points_order_button_shown` — вход по кнопке «Войти в аккаунт» на главной, через «Личный кабинет», через ссылку в форме регистрации и в форме восстановления пароля (параметризованный).

### Личный кабинет (`tests/test_personal_account.py`)
- `test_go_to_personal_account_profile_opened` — переход в личный кабинет по клику на «Личный кабинет».
- `test_go_from_personal_account_to_constructor_constructor_opened` — переход из личного кабинета в конструктор по клику на «Конструктор» и на логотип Stellar Burgers (параметризованный).

### Выход из аккаунта (`tests/test_logout.py`)
- `test_logout_from_personal_account_login_page_opened` — выход из аккаунта по кнопке «Выход» в личном кабинете.

### Конструктор (`tests/test_constructor.py`)
- `test_constructor_click_tab_section_selected` — переход к разделам «Соусы» и «Начинки» (параметризованный).
- `test_constructor_click_buns_tab_buns_selected` — переход к разделу «Булки».
