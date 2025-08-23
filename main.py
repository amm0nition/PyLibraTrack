import sys
import os
import time
from config import get_connection

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def view_books():
    clear_screen()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, book_name, isbn, status FROM book_list")
        rows = cursor.fetchall()
        
        print("ID | Book Name | ISBN | Status")
        print("-" * 60)
        
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        time.sleep(3)
        print("Return to Main Menu?")
        return_menu = input("Input y/n: ")
        if (return_menu == "y"):
            main()
    except Exception as e:
        print("Failed to fetch data.")
        
    finally:
        cursor.close()
        conn.close()

def view_patrons():
    clear_screen()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patrons")
        rows = cursor.fetchall()
        
        print("ID | Patron Name | Email | Birthdate | Borrowed Book 1 | Book 1 Status | Book 1 Duetime | Borrowed Book 2 | Book 2 Status | Book 2 Duetime  | Borrowed Book 3 | Book 3 Status | Book 3 Duetime ")
        print("-" * 60)
        
        for row in rows:
            print(" | ".join(str(col) for col in row))
        time.sleep(3)
        print("Return to Main Menu?")
        return_menu = input("Input y/n: ")
        if (return_menu == "y"):
            main()
    except Exception as e:
        print("Failed to fetch data.")
        
    finally:
        cursor.close()
        conn.close()

def main():
    clear_screen()
    print("Select Menu:\n1. View Library Books\n2. View Patron List\n3. Exit.")
    select_menu = int(input("Enter the number: "))
    if (select_menu == 1):
        print("Viewing Library Books...")
        view_books()
    if (select_menu == 2):
        print("Viewing Patron List...")
        view_patrons()
    else: sys.exit(0)

if __name__ == "__main__":
    main()
