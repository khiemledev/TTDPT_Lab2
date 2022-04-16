import pymysql
import configparser

config = configparser.ConfigParser()
config.read("./app.cfg")


def get_connection():
    connection = pymysql.connect(
        host=config["mysql"]["host"],
        user=config["mysql"]["user"],
        password=config["mysql"]["password"],
        database=config["mysql"]["database"],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
