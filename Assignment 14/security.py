class Security:
    def __init__(self):
        self.attempts = {}

    def validate_pin(self, card_number, pin, correct_pin):
        if card_number not in self.attempts:
            self.attempts[card_number] = 0

        if self.attempts[card_number] >= 3:
            return False  # locked out

        if pin == correct_pin:
            self.attempts[card_number] = 0
            return True
        
        self.attempts[card_number] += 1
        return False

# Python sees class Security creates class structure