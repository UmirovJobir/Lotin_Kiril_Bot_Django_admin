import requests
import json
import smtplib
import sqlite3
from email.mime.text import MIMEText


class Analiz:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
        self.cur = self.conn.cursor()

    def chack_user(self, chat_id):
        sql = f"select * from app_users where chat_id = {chat_id}"
        self.cur.execute(sql)
        b = 0
        for i in self.cur:
            if i:
                b = b + 1
        return b

    def count_users(self):
        sql = "select count(chat_id) from app_users"
        self.cur.execute(sql)
        for i in self.cur:
            return i[0]

    def users_insert(self, chat_id, username):
        self.cur.executemany("""INSERT INTO app_users (chat_id, username, date) VALUES(?,?, datetime('now', 'localtime'))""", [(chat_id, username)])
        self.conn.commit()

    def is_premium(self, chat_id):
        sql = f"select is_premium from app_users where chat_id = {chat_id}"
        self.cur.execute(sql)
        for i in self.cur:
            return i[0]

    def replay_dictionary_words(self):
        sql = f"select lotin, kiril from app_dictionary"
        self.cur.execute(sql)
        return self.cur


#--------------------------------------------------------------------

    def send_email(self, to_send, message):
        sender = "umirovamak@gmail.com"
        password = "password"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        try:
            server.login(sender, password)
            msg = MIMEText(message)
            msg["Subject"] = "AgroZamin !"
            server.sendmail(sender, to_send, msg.as_string())
            #server.sendmail(sender, to_send, f"Subject: AgroZamin !\n{message}")

            return "The message was send successfully!"
        except:
            return "Check your login or password please!"

#data = Analiz()
# data.users_insert(123456, 'umirov')
#data.chack_user(chat_id=546546)
# data.count_users()
# data.is_premium(chat_id=583110117)
