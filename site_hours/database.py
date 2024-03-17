from datetime import datetime
from typing import List
from typing import Optional

import pytz as pytz
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    # колонка с айдишником юзера (не трогай)
    id: Mapped[int] = mapped_column(primary_key=True)
    # колонка с именем юзера (не трогай)
    name: Mapped[str] = mapped_column(String(30))
    # колонка с фамилией юзера (не трогай)
    fullname: Mapped[Optional[str]]

    # колонка с адресом юзера типо sobaka@gmail.com (не трогай)
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    # колонка с датой создания учетки в бд - базе данных (можешь удалить если хочешь, но лучше оставь)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(pytz.timezone("Asia/Yekaterinburg")),
                                                 nullable=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# класс, обрабатывающий маилы (эл. почту) юзеров (просто не трогай)
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


engine = create_engine("sqlite:///example.sqlite3", echo=True)

# Вот эта штучка на 59 строке позволяет тебе как бы сбрасывать бд. То есть просто удаляй  файлик example.sqlite3 и
# нажимай запустить файл database.py
Base.metadata.create_all(engine)
