import os
from automate import Automate  # Assure-toi que le fichier se nomme bien automate.py

def menu_principal():
    while True:
        # 1. Choix de l'automate
        print("\n" + "="*40)
        choix = input("Quel automate voulez-vous utiliser ? (1 à 44) ou 'q' pour quitter : ")

        if choix.lower() == 'q':
            print("Fermeture du programme.")
            break

        nom_fichier = f"tests/automate{choix}.txt"

        # Vérification de l'existence du fichier
        if not os.path.exists(nom_fichier):
            print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas dans le dossier 'tests/'.")
            continue

        # 2. Chargement et premier affichage
        mon_automate = Automate()
        mon_automate.lire_fichier(nom_fichier)
        
        print(f"\n--- Structure de l'automate n°{choix} ---")
        mon_automate.afficher()

        # 3. Analyse et Déterminisation
        if not mon_automate.est_deterministe():
            print("⚠️ Cet automate est NON-DÉTERMINISTE.")
            reponse = input("Voulez-vous le déterminiser ? (o/n) : ").lower()
            
            if reponse == 'o':
                # On remplace l'instance actuelle par sa version déterminisée
                mon_automate = mon_automate.determiniser()
                print("\n✨ Automate après déterminisation :")
                mon_automate.afficher()
            else:
                print("Conservation de l'automate original (AFN).")
        else:
            print("✅ Cet automate est déjà DÉTERMINISTE.")

        # 4. Autres analyses (Complet, Minimal...)
        # if mon_automate.est_complet():
        #     print("L'automate est complet.")
        # else:
        #     print("L'automate n'est pas complet.")

        # 5. Boucle de test de mots
        print("\n--- Phase de test de mots ---")
        while True:
            mot = input("Entrez un mot à tester (ex: 'abb') ou 'fin' pour changer d'automate : ")
            
            if mot.lower() == 'fin':
                break
            
            # Ici, on pourra appeler ta fonction de reconnaissance
            # resultat = mon_automate.reconnaitre_mots(mot)
            # if resultat:
            #     print(f"✔️ Le mot '{mot}' est RECONNU.")
            # else:
            #     print(f"❌ Le mot '{mot}' n'est PAS RECONNU.")
            
            print(f"(Note : La reconnaissance du mot '{mot}' sera active une fois la méthode implémentée.)")

if __name__ == "__main__":
    menu_principal()