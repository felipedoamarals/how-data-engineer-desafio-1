import sqlalchemy

class Database:
    def __init__(self, user, password, host, port, database_name):
        self._engine = None
        self._connection = None
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._database_name = database_name

    @property
    def engine(self):
        if not self._engine:
            db_string = f"postgresql://{self._user}:{self._password}@{self._host}:{self._port}/{self._database_name}"
            self._engine = sqlalchemy.create_engine(db_string)
        return self._engine

    def connect(self):
        if not self._connection:
            self._connection = self.engine.connect()

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None
        if self._engine:
            self._engine.dispose()
            self._engine = None