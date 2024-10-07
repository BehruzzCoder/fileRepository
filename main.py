import os
class fileRepository:
    def __init__(self,fayl:str):
        self.__fayl = fayl


    def write_lines(self, yangi_matn: list[str] | tuple[str] | set[str] ):
        with open("Repositoryy.txt", "a") as FILE1:
            for i in range(0, len(yangi_matn[0])):
                FILE1.write(yangi_matn[i])
                if i == "\n":
                    FILE1.write("\n")
        FILE1.close()


    def read_line(self, son:int=1):
        with open("Repositoryy.txt", "r") as FILE2:
            for i in range(son):
                FILE2.readline()


    def read(self,byt=0):
        with open("Repositoryy.txt", "r") as file:
            if byt > 0 and type(byt) == int:
                for line in range(byt):
                    print(file.read(1), end="")
                    if line == "\n":
                        break
            else:
                print(file.readline())
            file.close()


    def write(self,str=""):
        with open("Repositoryy.txt", "a") as f2:
            f2.write("\n")
            f2.write(str)
            f2.close()


    def delete(self):
        if os.path.exists(self.__fayl):
            os.remove(self.__fayl)

    def replace(self,new,old):
        with open('Repositoryy.txt', 'r') as fayl:
            satrlar = fayl.readlines()
        for i in range(len(satrlar)):
            if old in satrlar[i]:
                satrlar[i] = satrlar[i].replace(old, new)
        with open('Repositoryy.txt', 'w') as fayl:
            fayl.writelines(satrlar)


    def search(self,str):
        with open("Repositoryy.txt", "r") as f6:
            if str in f6.read():
                return True
            else:
                return False


    def rename(self):
        a = input("Yangi faylini kiriting: ")
        if os.path.exists(a):
            print(f"{a} bunday nomi fayl mavjud!")
        else:
            with open(a, "w") as f7:
                self.__fayl = a
                print(f"{a} fayl ozgaritildi")


FILE = fileRepository("FileRepository.txt")
