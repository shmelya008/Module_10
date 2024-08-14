from datetime import datetime
import multiprocessing

time_start = datetime.now()


def read_info(name):
    all_data = []
    file = open(name)
    while True:
        line = file.readline()
        all_data.append(line)
        if not line:
            break
    file.close()


file_names = 'file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'
for i in file_names:
    name = i
    read_info(name)

time_end = datetime.now()
time_res = time_end - time_start
print(f'Время выполнения программы {time_res}')

# Время выполнения программы линейно - 0:00:11.628566

# if __name__ == '__main__':
#     file_names = 'file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, file_names)
#     time_end = datetime.now()
#     time_res = time_end - time_start
#     print(f'Время выполнения программы {time_res}')

# Время выполнения программы в multiprocessing - 0:00:06.626044
