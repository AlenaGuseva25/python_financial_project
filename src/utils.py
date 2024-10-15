import os
import json
import logging

# используется для записи сообщений об ошибках в журнал
logger = logging.getLogger(__name__)


def financial_transactions(file_path):
    """Функция принимает на вход путь до JSON - файла и возвращает список
           словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        logger.error(f'Файл {file_path} не найден.')
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
# isinstance для проверки принадлежности объекта к определенному классу или типу данных(новый метод, запомнить)
            if isinstance(data, list):
                return data
            else:
                logger.error(f'Данные в {file_path} не являются списком.')
                return []
    except json.decoder.JSONDecodeError:
        logger.error('Ошибка декодирования JSON.')
        return []
