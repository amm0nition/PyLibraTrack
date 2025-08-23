# PyLibraTrack
A simple Library Management System built with Python and MySQL/MariaDB.

## Setup

Follow these steps to get PyLibraTrack running on your machine:

1. Clone the repository and navigate into it:
   git clone https://github.com/amm0nition/PyLibraTrack.git
   cd PyLibraTrack

2. Create a virtual environment and activate it:
   python -m venv venv
   On Windows: venv\Scripts\activate
   On macOS/Linux: source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure your database:
   - Make sure MySQL or MariaDB is installed and running.
   - Create a database for the library system (for example, `librarydb`).
   - Update the database credentials in your connection script (`main.py` or `config.py`).

5. Run the program:
   python main.py

6. Optional: Test the connection first to ensure your database is set up correctly.
