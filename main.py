import pandas as pd
# Импортируем созданный класс из папки src и файла reporter.py
from src.reporter import DataFrameReporter

def main():
    # 1. Загружаем данные из папки data/
    data = pd.read_csv('data/payments.csv')
    
    # 2. Инициализируем объект класса (можно использовать настройки по умолчанию)
    reporter = DataFrameReporter()
    
    # 3. Вызываем метод show_report для создания отчёта
    reporter.show_report(data, title="Итоговый отчёт по платежам:")

# Конструкция для безопасного запуска скрипта
if __name__ == '__main__':
    main()
