class MysqlCRUD:
    __database = None

    def __init__(self, database_mysql):
        self.database = database_mysql

    def save(self, table_name: str, data: list):
        column_expression = None
        placeholders = None
        table_meta_data = self.get_schema_name(table_name)
        # print('table_meta_data : ', table_meta_data)
        table_column = self.get_column(table_name)
        # print('table_column : ', table_column)
        schema = table_meta_data[0][0]
        name = table_meta_data[0][1]
        column_expression = ','.join(column[0] for column in table_column if column[0] != 'ID')
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {schema}.{name} ({column_expression}) VALUES ({placeholders})"
        print(query)

    def get_column(self, table_name: str):
        query = f"SELECT COLUMN_NAME , DATA_TYPE FROM " \
                f" INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
        # print(query)
        result = self.database.execute_query(str(query), values=None)
        return result

    def get_schema_name(self, table_name: str):
        query = f"select TABLE_SCHEMA, TABLE_NAME from information_schema.TABLES where TABLE_NAME = '{table_name}'"
        # print(query)
        result = self.database.execute_query(str(query), values=None)
        return result

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, mysql_database):
        self.__database = mysql_database
