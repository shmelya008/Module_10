from threading import Thread
from datetime import datetime
from time import sleep

time_start = datetime.now()


def white_words(word_count, file_name):
    count = 1
    for i in range(word_count):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(f"Какое-то слово № {count}" '\n')
        file.close()
        sleep(0.1)
        count += 1
    print(f"Завершилась запись в файл {file_name}")


white_words(10, 'example1.txt')
white_words(30, 'example2.txt')
white_words(200, 'example3.txt')
white_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Время выполнения программы {time_res}')
print()

time_start = datetime.now()

thr_1 = Thread(target=white_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=white_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=white_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=white_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Время выполнения программы {time_res}')

