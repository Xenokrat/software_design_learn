import json
import sqlite3
from typing import Dict, Protocol, override


class Storage(Protocol):
    def save(self, data: str) -> None: ...

    def retrieve(self, id: int) -> str | None: ...


class InMemoryStorage(Storage):
    def __init__(self) -> None:
        super().__init__()
        self._storage: Dict[int, str] = {}
        self._counter: int = 0

    @override
    def save(self, data: str) -> None:
        self._storage[self._counter] = data

    @override
    def retrieve(self, id: int) -> str | None:
        return self._storage.get(id)


class FileStorage(Storage):
    def __init__(self) -> None:
        super().__init__()
        self._file: str = "storage.json"
        self._storage: Dict[int, str] = {}
        self._load_from_file()

    @override
    def save(self, data: str) -> None:
        id = len(self._storage)
        self._storage[id] = data
        self._save_to_file()

    @override
    def retrieve(self, id: int) -> str | None:
        return self._storage.get(id)

    def _save_to_file(self) -> None:
        try:
            with open(self._file, "w") as f:
                json.dump(self._storage, f)
        except FileNotFoundError:
            return
        except Exception as e:
            print("Exception occured while saving", e)

    def _load_from_file(self) -> None:
        try:
            with open(self._file, "r+") as f:
                self._storage = json.load(f)
        except Exception as e:
            print("Exception occured while loading", e)


class DatabaseStorage(Storage):
    def __init__(self) -> None:
        super().__init__()
        self._database: str = "storage.db"
        self._storage: Dict[int, str] = {}
        self._load_from_database()

    @override
    def save(self, data: str) -> None:
        id = len(self._storage)
        self._storage[id] = data
        self._save_to_database()

    @override
    def retrieve(self, id: int) -> str | None:
        return self._storage.get(id)

    def _load_from_database(self) -> None:
        try:
            with sqlite3.connect(self._database) as con:
                cur = con.cursor()
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS 
                        storage (
                            id INTEGER PRIMARY KEY,
                            data TEXT NOT NULL
                        )
                    """
                )
                cur.execute(
                    """
                    SELECT 
                        id, data
                    FROM
                        storage
                    """
                )
                res = cur.fetchall()
                self._storage = {k: v for (k, v) in res}
        except Exception as e:
            print("Exception occured while loading from db: ", e)

    def _save_to_database(self) -> None:
        try:
            with sqlite3.connect(self._database) as con:
                cur = con.cursor()
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS 
                        storage (
                            id INTEGER PRIMARY KEY,
                            data TEXT NOT NULL
                        )
                    """
                )
                print(list(self._storage.items()))
                for itm in self._storage.items():
                    cur.execute(
                        "INSERT OR IGNORE INTO storage (id, data) VALUES (?, ?)",
                        itm,
                    )
        except Exception as e:
            print("Exception occured while saving to db: ", e)


def main() -> None:
    memory_storage = InMemoryStorage()
    memory_storage.save("Data in memory")
    print(f"InMemoryStorage: {memory_storage.retrieve(0)}")

    file_storage = FileStorage()
    file_storage.save("Data in file")
    print(f"FileStorage: {file_storage.retrieve(0)}")

    db_storage = DatabaseStorage()
    db_storage.save("Data in database")
    print(f"DatabaseStorage: {db_storage.retrieve(0)}")


if __name__ == "__main__":
    main()
