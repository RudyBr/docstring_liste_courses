class Liste(list):
    def __init__(self, name):
        self.name = name

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("On ne peut ajouter qu'une chaîne de caractère.")
        if element in self:
            print(f"{element} est déjà dans la liste")
            return False
        self.append(element)
        return True
       


if __name__ == "__main__":
    print("test")
        
