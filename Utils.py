import os
import re
import math
import socket
import datetime
import random
import string

class Utils:
    @staticmethod
    def slugify(text):
        text = re.sub(r'[^\w\s-]', '', text).strip().lower()
        return re.sub(r'[-\s]+', '-', text)

    @staticmethod
    def factorial(n):
        return math.factorial(n)

    @staticmethod
    def read_file(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_file(path, content):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def current_timestamp():
        return datetime.datetime.now().isoformat()

    @staticmethod
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except:
            ip = '127.0.0.1'
        finally:
            s.close()
        return ip

    @staticmethod
    def is_palindrome(text):
        t = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
        return t == t[::-1]

    @staticmethod
    def get_file_size(path):
        return os.path.getsize(path) if os.path.exists(path) else -1

    @staticmethod
    def to_camel_case(snake_str):
        parts = snake_str.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])
