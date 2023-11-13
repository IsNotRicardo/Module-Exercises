class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"{self.author}, wrote by {self.author}, has {self.pages} pages.")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print(f"{self.editor} is the chief editor of {self.name}.")


def main():
    new_magazine = Magazine("Donald Duck", "Aki Hyyppä")
    new_book = Book("Compartment No. 6", "Rosa Liksom", 192)

    new_magazine.print_information()
    new_book.print_information()


main()
