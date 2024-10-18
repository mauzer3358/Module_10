import datetime
import  multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8')as f:
        for lines in f:
            f.readline()
            all_data.append(lines)
    return all_data


filenames = [f'./Files/file {number}.txt' for number in
                 range(1, 5)]

# data1 = []
# start = datetime.datetime.now()
# for i in filenames:
#     data1 += read_info(i)
# end = datetime.datetime.now()
# print(end-start, 'Линейный')

if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in
                 range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start, 'Многопроцессорный')


