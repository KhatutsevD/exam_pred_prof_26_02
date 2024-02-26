import csv


def stream_counter(a_name, t_name, t_date, b_date='01.01.2002'):
    """Описание функции complex.



     Описание аргументов:

    a_name: имя артиста
    t_name: название трека
    t_date: дата выхода трека
    b_date: дата указанная в начале задания (по стандарту 01.01.2002)

    """

    b_d, b_m, b_y = [int(y) for y in b_date.split('.')]
    t_d, t_m, t_y = [int(y) for y in t_date.split('.')]
    m_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date_delay = sum([(365 + (y % 4 == 0)) for y in range(b_y, t_y)]) + sum(
        [m_days[m - 1] for m in range(b_m, t_m)]) + t_d - b_d

    result_streams = abs(date_delay / (len(a_name) + len(t_name))) * 10000

    return result_streams


file = [[y.replace('\n', '') for y in x.split(';')] for x in open('songs.csv', encoding='utf-8').readlines()[1:]]
