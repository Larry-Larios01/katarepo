from abc import ABC, abstractmethod
import csv
class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass


class CSVDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, newline='') as csvfile:

            reader = csv.DictReader(csvfile)
            csvfile.seek(0) 
            next(reader)

        return reader
        



class DatabaseDataSource(DataSource):
    def __init__(self, path, env):
        self.path= path
        self.env = env

    def read_data(self):
        cursor = self.connection.cursor()
        cursor.execute(self.query)
        rows = cursor.fetchall()
        # Convierte los resultados en una lista de diccionarios
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]


class DataSourceFactory:
    @staticmethod
    def create_data_source(source_type, path, env):
        if source_type == "csv":
            return CSVDataSource(path)
        elif source_type == "database":
            return DatabaseDataSource(path, env)
        else:
            raise ValueError(f"Unknown data source type: {source_type}")
