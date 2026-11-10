import argparse
import os
import random
import sys

from lib import write_grid


def parse_args(argv=None):
    """Lire et vérifier les options. Enzo."""
    raise NotImplementedError


def random_grid(nb_cells, seed):
    """Créer une grille aléatoire reproductible. John-Lucas."""
    raise NotImplementedError


def parse_grid(text):
    """Transformer le texte lu sur STDIN en grille. John-Lucas."""
    raise NotImplementedError


def initial_grid(args):
    """Grille de STDIN si fournie, sinon aléatoire. John-Lucas."""
    raise NotImplementedError


def count_neighbors(grid, row, col, periodic):
    """Compter les voisines vivantes d'une cellule. Arthur."""
    raise NotImplementedError


def next_generation(grid, periodic):
    """Calculer la génération suivante. Arthur."""
    raise NotImplementedError


def grid_to_text(grid, iteration):
    """Mettre une grille au format texte. Rajan."""
    raise NotImplementedError


def run_text(grid, max_iterations, periodic):
    """Afficher la dernière itération sur STDOUT. Rajan."""
    raise NotImplementedError


def run_images(grid, max_iterations, periodic, directory):
    """Écrire une image PNG par génération. Rajan."""
    raise NotImplementedError


def main():
    args = parse_args()
    try:
        grid = initial_grid(args)
    except ValueError as error:
        print(f"Erreur : {error}", file=sys.stderr)
        sys.exit(1)
    if args.output_type == "text":
        run_text(grid, args.max_iterations, args.periodic)
    else:
        run_images(grid, args.max_iterations, args.periodic,
                   args.output_directory)


if __name__ == "__main__":
    main()