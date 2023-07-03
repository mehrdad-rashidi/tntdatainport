from typing import Any

import mysql.connector


class MysqlDatabase:
    __connection = None
    __cursor = None
    __host = None
    __user = None
    __password = None
    __database = None

    def __init__(self, host_name, user_name, user_password, database_name) -> None:
        self.user = user_name
        self.password = user_password
        self.host = host_name
        self.database = database_name
        try:
            self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host,
                                                      database=self.database)
            if self.connection.is_connected():
                print('Connected to MySQL database')

        except mysql.connector.Error as e:
            print('Reason Error Connect to Database is : ', e.msg, ' Error Code : ', e.errno, 'SqlStat : ', e.sqlstate)
            exit()

    def execute_query(self, query, values=None):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query, values)
            result = self.cursor.fetchall() if self.cursor else []
            self.cursor.close()
            return result
        except mysql.connector.Error as error:
            print(f"Get an error for execute query{query} reason is {error}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def database(self):
        return self.__database

    @connection.setter
    def connection(self, mysql_connection):
        self.__connection = mysql_connection

    @cursor.setter
    def cursor(self, mysql_cursor):
        self.__cursor = mysql_cursor

    @host.setter
    def host(self, mysql_host):
        self.__host = mysql_host

    @user.setter
    def user(self, mysql_user):
        self.__user = mysql_user

    @password.setter
    def password(self, mysql_password):
        self.__password = mysql_password

    @database.setter
    def database(self, mysql_database):
        self.__database = mysql_database
