import re
from geo_calculator.rolling_stone.exceptions import InvalidPlayerNameException


class Player:
    def __init__(self):
        self.name = None
        self.score = 0

    def getName(self):
        return self.name

    def receive_score(self, score):
        self.score += score

    def _get_name_for_player_from_input(self):
        return input("Please enter your name: ")

    def prompt_for_name(self):
        name = self._get_name_for_player_from_input()

        if not name:
            raise InvalidPlayerNameException("Name must have at least one character")

        if not re.match(r"^[a-zA-Z ]+$", name):
            raise InvalidPlayerNameException(
                "Name can only contain alphabetic characters and spaces"
            )

        if "  " in name:
            raise InvalidPlayerNameException(
                "Name cannot have multiple spaces in a row"
            )

        self.name = name
