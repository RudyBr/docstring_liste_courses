from pathlib import Path
import json

import constants

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
       
    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False
    
    def afficher_liste (self):
        print(f"Ma liste de {self.name} : ")
        for element in self:
            print(f"- {element}")
        
    def sauvegarde(self):
        chemin = Path(constants.DATA_DIR) / f"{self.name}.json"
        if not Path.exists(constants.DATA_DIR):
            Path.mkdir(constants.DATA_DIR)
        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)
        
        return True

if __name__ == "__main__":
    liste = Liste("fruits")
    liste.ajouter("bananes")
    liste.ajouter("fraises")
    liste.afficher_liste()
    liste.sauvegarde()
        
