"""
Допустим у нас есть класс БД, который содержит достаточно универсальные
методы.
В одном случае мы хотим запускать их для создания ежедневных отчётов.
В другом случае эти же методы с другим аргументом могут использоваться для
еженедельных отчетов.
Можно переиспользовать этот класс, "посещая" его другим классом, который
содержит инструкции, какие методы и как нужно запускать.
(Получается простая реализация паттерна "Посетитель").
"""

from abc import ABC, abstractmethod
from enum import Enum


class DBTask(Enum):
    DAILY = 1
    WEEKLY = 2


class DBClient:
    def drop_category_table(): ...
    def create_category_table(): ...
    def insert_into_category_table(task: DBTask): ...
    def insert_into_main_table(task: DBTask): ...
    def drop_client_category_table(): ...
    def create_client_category_table(): ...
    def insert_into_client_category_table(task: DBTask): ...
    def insert_into_client_table(task: DBTask): ...


class DatabaseVisitor(ABC):
    @abstractmethod
    async def update_local_statistics(self, client: DBClient) -> None: pass

    @abstractmethod
    async def update_client_report(self, client: DBClient) -> None: pass


class DailyDatabaseVisitor(DatabaseVisitor):
    """
    "Посещает" задачи, которые нужно выполнять на ежедневной основе
    """
    async def visit_local_statistics(self, client: DBClient) -> None:
        await client.drop_category_table()
        await client.create_category_table()
        await client.insert_into_category_table(DBTask.DAILY)
        await client.insert_into_main_table(DBTask.DAILY)
        await client.drop_category_table()

    async def visit_client_report(self, client: DBClient) -> None:
        await client.drop_client_category_table()
        await client.create_client_category_table()
        await client.insert_into_client_category_table(DBTask.DAILY)
        await client.insert_into_client_table(DBTask.DAILY)
        await client.drop_client_category_table()


class WeeklyDatabaseVisitor(DatabaseVisitor):
    """
    "Посещает" задачи, которые нужно выполнять на еженедельной основе
    """
    async def visit_local_statistics(self, client: DBClient) -> None:
        await client.drop_category_table()
        await client.create_category_table()
        await client.insert_into_category_table(DBTask.WEEKLY)
        await client.insert_into_main_table(DBTask.WEEKLY)
        await client.drop_category_table()

    async def visit_client_report(self, client: DBClient) -> None:
        await client.drop_client_category_table()
        await client.create_client_category_table()
        await client.insert_into_client_category_table(DBTask.WEEKLY)
        await client.insert_into_client_table(DBTask.WEEKLY)
        await client.drop_client_category_table()
