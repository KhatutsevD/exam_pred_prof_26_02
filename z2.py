def forward_or_back(arr_in, arr_new):
    i_d, i_m, i_y = [int(y) for y in arr_in[3].split('.')]
    n_d, n_m, n_y = [int(y) for y in arr_new[3].split('.')]
    if i_y != n_y:
        return i_y < n_y
    elif i_m != n_m:
        return i_m < n_m
    else:
        return i_d < n_d


file = [[y.replace('\n', '') for y in x.split(';')] for x in open('songs.csv', encoding='utf-8').readlines()[1:]]
