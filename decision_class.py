import random
import re

# Creating a class for the decision maker


class DecisionMaker:
    def __init__(self, options):  # Initialize the decision maker
        self.options = options

    def make_decision_simple(self):    # Decision maker without weights
        return random.choice(re.split(',|ou', self.options)).title()

    def make_decision_weighted(self, weights):  # Decision maker with weights
        weights = weights.split(',')
        weights = [int(i) for i in weights]
        return random.choices(re.split(',|ou', self.options), weights=weights, k=1)[0].title()
