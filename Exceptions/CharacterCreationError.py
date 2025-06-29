class CharacterCreationError(Exception):
    def __init__(self, message="Error during character creation occured."):
        self.message = message
        super().__init__(self.message)