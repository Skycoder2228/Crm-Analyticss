from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Client, Report
from db import create_db

# Создаем соединение с базой данных
engine = create_engine('sqlite:///crm.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

create_db()  # Создание таблиц

# Добавляем пользователя
new_user = User(username='admin', password='password')
session.add(new_user)
session.commit()

# Добавляем клиента
new_client = Client(name="Иван Иванов", email="ivan@example.com", phone="+79876543210")
session.add(new_client)
session.commit()

# Добавляем отчет
report_data = 'Данные отчета...'.encode('utf-8')  # Кодируем строку в UTF-8
new_report = Report(client=new_client, data=report_data)
session.add(new_report)
session.commit()

# Запрашиваем список всех клиентов
clients = session.query(Client).all()
for client in clients:
    print(f"{client.name}, {client.email}")

# Закрываем сессию
session.close()