#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Клонирование и инициализация репозитория
mkdir my_folder
cd my_folder
git clone https://github.com/askras/aads.git
cd aads

# Создание виртуального окружения и получение зависимостей
python -m venv venv
. ./venv/bin/activate
python -m pip install pip --upgrade
python -m pip install -r requirements.txt

# Запуск jupyter notebook
jupyter notebook

# Отправка результатов в github
git status
git add labs/lab01/lab01_XX/
git status
git commit -m 'Описание коммита'
git push origin
