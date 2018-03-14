import time

def ajoute_deux(une_valeur, results=None, index=None):
    time.sleep(3)  # simule un traitement qui prend 3 secondes
    resultat = une_valeur + 2
    if results:
        if 0 <= index < len(results):
            results[index] = resultat
    return resultat