class Author():
    
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    
    def get_info(self):
        return f"{self.name} : {self.biography}"