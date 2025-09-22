from src.administrator import Administrator
from src.file_reader import FileReader


def main():
    args = FileReader.parse_file("attendance_weekday_500.txt")
    admin = Administrator()
    admin.update(args)
    admin.print_result()


main()