class Personne(object):
    
    annee_actuelle = 2018  # variable de classe, partagée par toutes les instances de Personne
    # En pratique, on récupèrera l'année actuelle autrement.
    
    def __init__(self, nom=None, prenom=None, annee_de_naissance=2000):
        self.nom = nom
        self.prenom = prenom
        self.annee_de_naissance = annee_de_naissance
        
    def age(self):
        # une version simplifiée pour calculer l'age
        return self.annee_actuelle - self.annee_de_naissance
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):  # Surcharge de la fonction __str__() pour les instances de Personne
        return "{} {} est une Personne agée de {} ans.".format(self.prenom, self.nom, self.age())
    
    
class Employe(Personne):
    def __init__(self, employeur=None, **kwargs):
        super().__init__(**kwargs)
        self.employeur = employeur
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):  # Surcharge de la fonction __str__() pour les instances d'Employe
        return super().__str__() + " C'est un employé de {}.".format(self.employeur)