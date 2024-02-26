def forward_or_back(arr_in, arr_new):
    i_d, i_m, i_y = [int(y) for y in arr_in[3].split('.')]
    n_d, n_m, n_y = [int(y) for y in arr_new[3].split('.')]
    if i_y != n_y:
        return i_y > n_y
    elif i_m != n_m:
        return i_m > n_m
    elif i_d != n_d:
        return i_d > n_d
    return False


file = [[y.replace('\n', '') for y in x.split(';')] for x in open('songs.csv', encoding='utf-8').readlines()[1:]]

new_file = [file[0]]

k = 0

print(forward_or_back(['', '', '', '14.07.2023'], ['', '', '', '30.06.2023']))

for row in file[1:10]:
    i = 0
    while len(new_file) >= abs(i) and forward_or_back(new_file[i], row):
        i -= 1
    print(i)
    if i == 0:
        new_file = new_file +[row]
    elif abs(i) < len(new_file):
        new_file = new_file[:i] + [row] + new_file[i:]
    else:
        new_file = [row] + new_file
    k += 1
    print(f'ПРОХОД {k}')
    print(*[x[3] for x in new_file], sep='\n')

