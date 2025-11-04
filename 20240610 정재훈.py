class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class Book:
    def __init__(self, book_id, title, author, year):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"책 번호 : {self.id} , 제목 : {self.title} , 저자 : {self.author} , 출판연도 : {self.year}"


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert_front(self, book):
        new = Node(book, self.head)
        self.head = new

    def display(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.link

    def find_by_title(self, title):
        current = self.head
        while current:
            if current.data.title == title:
                return current.data
            current = current.link
        return None

    def exists_book_id(self, book_id):
        current = self.head
        while current:
            if current.data.id == book_id:
                return True
            current = current.link
        return False

    def exists_book_title(self, title):
        current = self.head
        while current:
            if current.data.title == title:
                return True
            current = current.link
        return False

    def remove_by_title(self, title):
        if self.isEmpty():
            return False

        if self.head.data.title == title:
            self.head = self.head.link
            return True

        prev = self.head
        while prev.link:
            if prev.link.data.title == title:
                prev.popNext()
                return True
            prev = prev.link
        return False


class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.book_list.exists_book_id(book_id):
            print("이미 존재하는 책 번호입니다.")
            return
        if self.book_list.exists_book_title(title):
            print("이미 존재하는 책 제목입니다.")
            return
        book = Book(book_id, title, author, year)
        self.book_list.insert_front(book)
        print("도서가 추가되었습니다.")

    def remove_book(self, title):
        if self.book_list.remove_by_title(title):
            print("도서가 삭제되었습니다.")
        else:
            print("해당 제목의 도서가 존재하지 않습니다.")

    def search_book(self, title):
        book = self.book_list.find_by_title(title)
        if book:
            print(book)
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    def display_books(self):
        self.book_list.display()

    def run(self):
        while True:
            print("\n====== 도서 관리 프로그램 ======")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로)")
            print("3. 도서 조회 (책 제목으로)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            choice = input("메뉴 선택: ")

            if choice == "1":
                book_id = input("책 번호: ")
                title = input("책 제목: ")
                author = input("저자: ")
                year = input("출판 연도: ")
                if book_id.strip() == "" or title.strip() == "":
                    print("책 번호와 제목은 반드시 입력해야 합니다.")
                    continue
                self.add_book(book_id, title, author, year)

            elif choice == "2":
                title = input("삭제할 책 제목: ")
                self.remove_book(title)

            elif choice == "3":
                title = input("조회할 책 제목: ")
                self.search_book(title)

            elif choice == "4":
                self.display_books()

            elif choice == "5":
                print("프로그램을 종료합니다.")
                break

            else:
                print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
