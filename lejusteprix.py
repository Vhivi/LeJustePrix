#!/usr/bin/python
# -*- coding: utf-8 -*-

# Projet de "Juste prix",
# Le programme génère un prix entier aléatoire dans une fourchette définie par
# l'utilisateur. Le but pour l’utilisateur est de deviner le prix. Chaque fois
# que l’utilisateur se trompe, l’ordinateur lui dit si c’est plus ou moins que
# le prix qu’il a donné. À chaque aide de l’ordinateur, le score final
# atteignable par le joueur baisse.

# Au programme, vous apprendrez à saisir des entrées clavier par un
# utilisateur, créer des fonctions pour valider que le nombre entré est bien
# un nombre entier, comparer une variable de référence (le prix) avec une
# autre variable et de calculer la différence entre deux nombre.

import random


# Génération aléatoire d'un prix entier.
def generation_alea_prix(prixmax):
    return random.randint(0, prixmax)


def main():
    # Demander le prix max.
    prixmax = int(input("Quel est le prix maximum de la session de jeu ?"))

    justeprix = generation_alea_prix(prixmax)

    # Deviner le prix généré.
    # Si l'utilisateur se trompe, on baisse le score final.
    # Et on lui dit si son entrée est plus ou moins que le prix généré.
    prixuser = 0
    scoremin = 0
    scoremax = 10
    scoreuser = scoremax
    while prixuser != justeprix:
        prixuser = int(input("Quel est selon vous le prix ?"))
        if scoreuser == scoremin:
            print("Votre score est de ", scoreuser)
            print("Vous avez perdu !")
            print("Le juste prix est de", justeprix)
            break

        if prixuser == justeprix:
            print("Bravo !!! Vous avez découvert le juste prix.")
            print("Score :", scoreuser)
            break

        if prixuser < justeprix:
            print("C'est plus !")
            scoreuser = scoreuser - 1

        if prixuser > justeprix:
            print("C'est moins !")
            scoreuser = scoreuser - 1


main()
