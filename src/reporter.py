class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title:
            print(title)

        print('Количество столбцов:', df.shape[1])
        print('Количество строк:', df.shape[0])

        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)

        # Защита от деления на 0 на случай пустого DF
        duplicates_share = duplicates / df.shape[0] if df.shape[0] > 0 else 0.0
        print('Доля дубликатов:', format(duplicates_share, self.percent_format))

        # Вывод сводной статистики describe
        print(df.describe(include='all' if self.include_all else None))

        # Количество пропусков во всем датафрейме
        print('Количество пропусков:', df.isna().sum().sum())

        # Доля пропусков во всем датафрейме в формате float_format
        print('Доля пропусков:', format(df.isna().mean(axis=None), self.float_format))