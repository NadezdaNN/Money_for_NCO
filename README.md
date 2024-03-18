## Тема проекта. Государственные деньги для НКО

## Оглавление  
[1. Описание и цель проекта](./README.md#Описание-и-цель-проекта)  
[2. Постановка задачи](./README.md#Постановка-задачи)    
[3. Структура проекта](./README.md#Структура-проекта)  
[4. Как установить проект](./README.md#Как-установить-проект)    
[5. Ссылка на датасет и другие файлы](./README.md#Ссылка-на-датасет-и-другие-файлы)  
[6. Ссылка на docker-образ для запуска модели предсказания в контейнере](./README.md#Ссылка-на-docker-образ-для-запуска-модели-предсказания-в-контейнере)

### Описание и цель проекта    
НКО хотят повысить свои шансы на получение грантов/субсидий/госконтрактов от государства. Для этого им важно понять, что именно может повлиять на это. Результаты исследования можно использовать для того, чтобы подсказывать НКО, как повысить шансы на финансовую поддержку.
Цель — спрогнозировать вероятность получения грантов/субсидий/госконтрактов от государства для организации в зависимости от её характеристик:
* от региона регистрации организации;
* от возраста организации;
* от экономической деятельности организации; 
* от организационно-правовой формы (ОПФ/ОКОПФ);
* от формы НКО;
* от наличия записей организации в соц.сетях (её публичности).

### Постановка задачи
В нашем распоряжении есть дамп данных обо всех НКО России (актуален на 26.08.2021), в котором
содержится информация о получении государственных грантов,
госконтрактов и субсидий, регионе и дате регистрации, а также ОКВЭД
(классификатор экономической деятельности).

Необходимо проверить, есть ли зависимость вероятности получения
грантов/госконтрактов от государства от региона регистрации, возраста, экономической деятельности, а так же, от организационно-правовой формы, от формы НКО и от наличия записей организации в соц.сетях (её публичности).

### Структура проекта
1. Сбор данных
2. Анализ, обработка и визуализация данных. Кодирование признаков. Решение задачи классификации. Подготовка модели к продакшену.
3. Деплой модели

### Как установить проект
Выполнить следующие команды в терминале:
1. git clone https://github.com/NadezdaNN/Money_for_NGO.git
2. Создать виртуальное окружение (в Windows): python -m venv .venv
3. Активировать его (в Windows): .venv/Scripts/Activate.ps1
4. Установить зависимости: pip install -r requirements.txt

### Ссылка на датасет и другие файлы
https://drive.google.com/drive/folders/1EO_OeOH7WoFX7LSlHmrJ1eNsebfWauPv?usp=sharing

### Ссылка на docker-образ для запуска модели предсказания в контейнере
https://hub.docker.com/repository/docker/nadezdann/ngo_image/general
