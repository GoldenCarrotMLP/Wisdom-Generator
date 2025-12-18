from collections import deque

class QuoteHistory:
    def __init__(self, limit=100):
        self.history = deque(maxlen=limit)

    def add(self, quote):
        self.history.append(quote)

    def get(self):
        return list(self.history)