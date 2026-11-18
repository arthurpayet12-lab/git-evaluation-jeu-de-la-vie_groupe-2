import argparse
import os
import random
import sys

from lib import write_grid

def parse_args():
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


    return parser.parse_args()

def random_grid(nb_cells, seed):
    """Créer une grille aléatoire reproductible. John-Lucas."""
    rng = random.Random(seed)
    return [[rng.randint(0, 1) for _ in range(nb_cells)] for _ in range(nb_cells)]


def parse_grid(text):
    """Transformer le texte lu sur STDIN en grille. John-Lucas."""
    raise NotImplementedError


def initial_grid(args):
    """Grille de STDIN si fournie, sinon aléatoire. John-Lucas."""
    raise NotImplementedError


def count_neighbors(grid, row, col, periodic):
    """Compter les voisines vivantes d'une cellule. Enzo."""
    raise NotImplementedError


def next_generation(grid, periodic):
    """Calculer la génération suivante. Enzo."""
    raise NotImplementedError


def grid_to_text(grid, iteration):
    """Mettre une grille au format texte. Enzo."""
    raise NotImplementedError


def run_text(grid, max_iterations, periodic):
    """Afficher la dernière itération sur STDOUT. Rajan."""
    raise NotImplementedError


def run_images(grid, max_iterations, periodic, directory):
    """Écrire une image PNG par génération. Rajan."""
    raise NotImplementedError



def main():
    nb_cells = 50

    rng = random.Random(4200)

    matrix = [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

    iter = 0
    filename = f"outputs/grid_{iter:04d}.png"
    write_grid(matrix=matrix, filename=filename)

if __name__ == "__main__":
    main()
