
def get_shelfs_book(new_shelfs):
    for i in range(new_shelfs):
        shelf_number = int(input("Куда вы хотите поставить книгу?: "))
        name_book = input("Введите название книги: ")
        authors = input("Введите автора книги: ")
        shelfs_format = "{'book_name': name_book, 'authors': authors}"

        with open("library.txt", "a") as f:
            f.write(f"Shelf_{shelf_number}: {shelfs_format}\n")

    return "Книги добавлены"


def read_file_library():
    with open("library.txt", "r") as f:
        for line in f:
            print(line.strip())


def main():
    new_shelfs = int(input("Сколько книг вам нужно добавить?: "))
    print(get_shelfs_book(new_shelfs))
    read_file_library()


if __name__ == "__main__":
    main()
