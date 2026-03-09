import sqlite3

def create_db():
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Таблица клиентов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE NOT NULL
        )
    ''')

    # Таблица отчетов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY,
            client_id INTEGER NOT NULL,
            report_date DATE NOT NULL,
            data BLOB NOT NULL,
            FOREIGN KEY(client_id) REFERENCES clients(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()