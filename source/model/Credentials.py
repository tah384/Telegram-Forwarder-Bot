import json
import os.path

from source.utils.Constants import CREDENTIALS_FILE_PATH


class Credentials:

    def __init__(self, api_id=None, api_hash=None, phone_number=None):
        self.api_id = 29426486
        self.api_hash = d71ad4ec048ab41677a1a439b21ff0c9
        self.phone_number = +923052432382

    def write(self):
        with open(CREDENTIALS_FILE_PATH, "w") as file:
            json.dump(self.__dict__, file, indent=4)

    @staticmethod
    def read():
        with open(CREDENTIALS_FILE_PATH, "r") as file:
            data = json.load(file)
            return Credentials(**data)

    @staticmethod
    def scan():
        credentials = Credentials()
        credentials.api_id = input("Enter your API ID: ")
        credentials.api_hash = input("Enter your API Hash: ")
        credentials.phone_number = input("Enter your phone number: ")
        credentials.write()
        return credentials

    @staticmethod
    def get(is_saved=False):
        if is_saved and os.path.exists(CREDENTIALS_FILE_PATH):
            return Credentials.read()
        else:
            return Credentials.scan()
