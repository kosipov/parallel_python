import threading


def my_func(thread_number):
    return print('my_func called by thread N°{}'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))#инициализируем поток
        threads.append(t)
        t.start() #стартуем поток
        t.join() #передаем управление потоку

if __name__ == "__main__":
    main()
