from .perceptions_options import (
    VALID_POSSIBLE_PERCEPTIONS_BODIES,
    VALID_POSSIBLE_PERCEPTIONS_ARGS,
)

from random_words import RandomWords
from random import choice, shuffle
from time import time


class PerceptionGenerator:
    def __init__(self, perceptions_number, invalid_perceptions_percentage):
        self.perceptions_number = perceptions_number
        self.invalid_p = invalid_perceptions_percentage
        self.valid_p = 100 - invalid_perceptions_percentage

    def generate(self):
        start_time = time()

        valid = []
        invalid = []

        valid_perceptions_number = int(self.valid_p * self.perceptions_number / 100)
        invalid_perceptions_number = int(self.invalid_p * self.perceptions_number / 100)

        random_words = RandomWords()
        bodies = random_words.random_words(count=invalid_perceptions_number)
        args = random_words.random_words(count=invalid_perceptions_number)

        for i in range(valid_perceptions_number):
            body = choice(VALID_POSSIBLE_PERCEPTIONS_BODIES)
            arg = choice(VALID_POSSIBLE_PERCEPTIONS_ARGS)

            perception = f"{body}({arg})"
            valid.append(perception)

        for i in range(invalid_perceptions_number):
            body = bodies.pop(0).lower()
            arg = args.pop(0).lower()

            perception = f"{body}({arg})"
            invalid.append(perception)

        perceptions = valid + invalid
        shuffle(perceptions)

        file = open("perceptions.txt", "w")

        for line in perceptions:
            file.write(line)
            file.write("\n")

        file.close()

        final_time = time() - start_time
        print(f"{self.perceptions_number} perceptions generated in {final_time}")
