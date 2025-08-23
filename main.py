import sys
import mysql.connector
from mysql.connector import Error

def main():
    print("Select Menu:\n1. View Library Books\n2. View Patron List\n3. Exit.")
    select_menu = input("Enter the number: ")
    if (select_menu == 1):
        print("Viewing Library Books...")
    if (select_menu == 2):
        print("Viewing Patron List...")
    else: sys.exit(0)

if __name__ == "__main__":
    main()
