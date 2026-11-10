import argparse
import os
import random
import sys

from lib import write_grid



def parse_args(argv=None):
    """Lit les options de la ligne de commande et renvoie le résultat d'argparse.

    Options : -n/--nb_cells, -m/--max_iterations, -s/--seed,
    -o/--output_directory, -t/--output_type, -p/--periodic (et -h/--help).
    Vérifier que nb_cells > 0 et max_iterations >= 0.
    """
    parser = argparse.ArgumentParser(description="Jeu de la vie de Conway")

    parser.add_argument("-n", "--nb_cells", type=int, default=10,
                        help="nombre de cellules par côté pour une grille aléatoire (défaut : 10)")
    parser.add_argument("-m", "--max_iterations", type=int, default=20,
                        help="numéro de la dernière itération à calculer (défaut : 20)")
    parser.add_argument("-s", "--seed", type=int, default=42,
                        help="graine du générateur aléatoire (défaut : 42)")
    parser.add_argument("-o", "--output_directory", default="outputs",
                        help="dossier dans lequel écrire les images (défaut : outputs)")
    parser.add_argument("-t", "--output_type", choices=["image", "text"], default="image",
                        help="type de sortie : image ou text (défaut : image)")
    parser.add_argument("-p", "--periodic", action="store_true",
                        help="active les conditions aux limites périodiques")

    args = parser.parse_args(argv)

    if args.nb_cells <= 0:
        parser.error("nb_cells doit être strictement positif (> 0)")

    if args.max_iterations < 0:
        parser.error("max_iterations doit être supérieur ou égal à zéro (>= 0)")

    return args



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