from utils.gemini_client import generate_batch

class QuoteBuffer:
    def __init__(self, batch_size=30):
        self.batch_size = batch_size
        self.quotes = []
        self.index = 0

    def refill(self):
        self.quotes = generate_batch()
        self.index = 0

    def next_quote(self):
        if not self.quotes or self.index >= len(self.quotes):
            self.refill()
        quote = self.quotes[self.index]
        self.index += 1
        return quote