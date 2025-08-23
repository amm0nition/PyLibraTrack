import sys
import mysql.connector
from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='libra_user',
#         password='libra_pass',
#         database='libratrack_db'
#     )

#     if connection.is_connected():
#         print("Connection successful!")
#         db_info = connection.server_info
#         print("MariaDB/MySQL server version:", db_info)

# except Error as e:
#     print("Error while connecting:", e)

# finally:
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("Connection closed.")

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
