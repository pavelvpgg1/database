# не нужный файл, просто оставить для примера

from database import engine, User

from sqlalchemy.orm import Session


# Вот эта хренотень позволяет тебе добавлять юзеров в бд
with Session(bind=engine) as session:
    # В переменной "user" хранятся его параметры по типу имени и фамилии
    # Вот в парамертры "name" и "fullname" ты должен вставлять те данные,
    # которые ты будешь принимать с фронта и распарсивать их
    # на остальные поля внимания не обращай, просто не трогай их
    user = User(name="Test", fullname='Full test')
    session.add(user)
    session.commit()

    user = session.query(User).first()
    # этот принт можешь удалить, он просто выводит отчет о создании учетки
    print(user)
