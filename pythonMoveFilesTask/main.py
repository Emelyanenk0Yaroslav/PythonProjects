import shutil
import os

class Pair:

    """Класс Pair отвечает за пары каталогов: Папки-Источника(src) и Папки-Назначения(dst), а также за Маску файла(mask)"""

    def __init__(self, src, dst, mask):
        self.src = src
        self.dst = dst
        self.mask = mask
def info(Pair,operations_counter, sum_of_errors, src_nf, dst_nf, no_file_access):

    """Эта функция предназначена для вывода информации и вызывается из функции move"""

    print(f"Всего операций: {operations_counter} \nВсего ошибок: {sum_of_errors}")
    print((f"Источник не найден: {src_nf} | Папка назначения не найдена: {no_file_access} | Ошибка доступа: {no_file_access}"))
def move(Pair):

    """Функция move отвечает за транспортировку файлов"""

    """Главная беда - счётчики, решил остановиться на таком безобразном решении"""
    operations_counter = 0
    sum_of_errors = 0
    src_nf = 0
    dst_nf = 0
    no_file_access =0


    src = Pair.src
    dst = Pair.dst
    mask = Pair.mask

    """Здесь получаем список файлов и директорий в каталоге"""
    files = os.listdir(src)


    for file in files:

        """Для у каждого файла из полученного списка мы проверяем маску и если она совпадает, то пытаемся переместить их """

        if file.endswith(mask):
            src_file = os.path.join(src,file)
            dst_file = os.path.join(dst,file)

            try:
                shutil.move(src_file,dst_file)
                operations_counter +=1
                print(f"Файл:{file} с расширением:{Pair.mask} был перемещен из директории: {src} в {dst} ")
            except:
                if not os.path.exists(src):
                    src_nf += 1
                    print("")
                elif not os.path.exists(dst):
                    dst_nf += 1
                    print("Папка назначения не найдена")
                else:
                    "Не удалось скопировать файл"
                sum_of_errors += 1

    info(Pair,operations_counter, sum_of_errors, src_nf, dst_nf, no_file_access)


test = Pair("C:/Users/Ryzen5/Desktop/Doc", "C:/Users/Ryzen5/Desktop/NewDoc",".jpg")
move(test)