class Library:
    def __init__(self , listOfbooks):
        self.books=listOfbooks
    
    def book(self):
        for i in self.books:
            print(i)

    def borrowBook(self, BookName):
        if BookName in self.books:
            print(f"You sucessfully borrowed the book {BookName}")
            self.books.remove(BookName)
        else:
            print(f"The book {BookName} is not present try ot acces it later")

    def returnBook(self, ReBooks) :
        print(f"you book {ReBooks} have been sucessfully returned")
        self.books.append(ReBooks)

class Student:
    def requestBook(self):
        self.req=input("Enter the book that you want:  ")
        return self.req
    
    def returnBook(self):
        self.ret = input("Enter the Book that you want ot return: ")
        return self.ret
    
if __name__=="__main__":
    centrallibrary=Library(["Django", "Python", "Flask", "Pandas","Machine Learning"])
    student=Student()

    while(True):
        a='''----------------------------------Welcome to Library-------------------------------------
        Read the below instruction:
        1. list of all the books ----> press 1
        2. Request a Book ----> press 2
        3. Return the Book ----> press 3
        4. To close the library ---> press 4
        '''

        print(a)
        
        message=int(input("Enter what you want: "))
        if message==1:
            centrallibrary.book()
        elif message==2:
            centrallibrary.borrowBook(student.requestBook())
        elif message==3:
            centrallibrary.returnBook(student.returnBook())
        elif messsage==4:
            exit()

        
