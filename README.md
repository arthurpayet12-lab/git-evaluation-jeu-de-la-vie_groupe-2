# Jeu de la vie — Groupe 2

Simulation en Python du [jeu de la vie de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie). Le programme `main.py` génère une grille aléatoire ou lit une grille sur l'entrée standard, puis calcule son évolution avec des conditions aux limites fixes ou périodiques. Le résultat est écrit sous forme d'images PNG (une par génération) ou en texte sur la sortie standard.

- [Installation](#installation)
- [Exécution](#exécution)
- [Arguments](#arguments)
- [Vidéos](#vidéos)
- [Auteurs](#auteurs)
- [Liens utiles](#liens-utiles)

## Installation

### Programme

Le programme n'utilise que la bibliothèque standard de Python et le fichier `lib.py` fourni. Il suffit d'avoir **Python 3.10 ou plus récent** et Git :

```bash
git clone https://github.com/arthurpayet12-lab/git-evaluation-jeu-de-la-vie_groupe-2.git
cd git-evaluation-jeu-de-la-vie_groupe-2
python3 --version
```

### Outils vidéo

Les vidéos nécessitent [`ffmpeg`](https://ffmpeg.org/) et [Gource](https://gource.io/).

- **Ubuntu / Debian** :

  ```bash
  sudo apt update
  sudo apt install python3 git gource ffmpeg
  ```

- **macOS** (avec [Homebrew](https://brew.sh/)) :

  ```bash
  brew install gource ffmpeg
  ```

- **Windows** : installer [WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) depuis un PowerShell administrateur avec `wsl --install`, puis suivre les commandes Ubuntu dans le terminal WSL.

Vérifier l'installation :

```bash
gource --version
ffmpeg -version
```

### Tests

Depuis la racine du dépôt :

```bash
sh check_script_options.sh
sh check_tests.sh
```

Les deux scripts doivent se terminer par `Nb test success: 6 / 6` et `Nb test success: 74 / 74`.

## Exécution

### Sans option : images avec les valeurs par défaut

Une grille aléatoire de 10 × 10 (graine `42`) évolue jusqu'à l'itération 20. Les 21 images sont écrites dans `outputs` :

```bash
$ python3 main.py
Generation of 21 images in directory outputs
$ ls -p1 outputs | wc -l
      21
```

Les fichiers se nomment `grid_0000.png` à `grid_0020.png`.

### Grille aléatoire personnalisée

```bash
$ python3 main.py -n 50 -m 200 -s 4200
Generation of 201 images in directory outputs
```

### Lire une grille sur l'entrée standard

La première ligne contient la taille de la grille, suivie des lignes de la matrice (cellules `0` ou `1` séparées par des espaces) :

```text
3
1 0 1
0 0 1
1 0 1
```

Avec `-t text`, seule la dernière itération est affichée :

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
iteration: 1
0 1 0
0 0 1
0 1 0
```

La redirection `<` fonctionne aussi :

```bash
$ python3 main.py -m 2 -t text < tests/matrix4/input.txt
iteration: 2
0 0 1 0
0 1 0 1
0 1 0 1
0 0 1 0
```

### Conditions aux limites périodiques

Avec `-p`, les bords opposés de la grille sont reliés (surface d'un tore) :

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
iteration: 1
0 0 0
0 0 0
0 0 0
```

### Images dans un autre dossier

```bash
$ python3 main.py -n 30 -m 50 -o mes_images
Generation of 51 images in directory mes_images
```

### Gestion des erreurs

Une entrée invalide produit un message sur la sortie d'erreur et un code de sortie différent de `0` :

```bash
$ printf '2\n1 2\n0 0\n' | python3 main.py -t text
Erreur : valeur invalide : 2
$ echo $?
1
$ python3 main.py -m -1
usage: main.py [-h] [-n NB_CELLS] [-m MAX_ITERATIONS] [-s SEED]
               [-o OUTPUT_DIRECTORY] [-t {image,text}] [-p]
main.py: error: max_iterations doit être supérieur ou égal à zéro (>= 0)
$ echo $?
2
```

Sont refusés : une grille vide ou mal formée, une cellule différente de `0` ou `1`, une taille non positive, `--nb_cells` ≤ 0, `--max_iterations` < 0 et un type de sortie autre que `image` ou `text`.

## Arguments

| Option courte | Option longue | Description | Valeur par défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | nombre de cellules par côté pour une grille aléatoire (entier > 0) | `10` |
| `-m N` | `--max_iterations N` | numéro de la dernière itération à calculer (entier ≥ 0) | `20` |
| `-s N` | `--seed N` | graine du générateur aléatoire (entier quelconque) | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier dans lequel écrire les images | `outputs` |
| `-t TYPE` | `--output_type TYPE` | type de sortie : `image` ou `text` | `image` |
| `-p` | `--periodic` | active les conditions aux limites périodiques | désactivée |
| `-h` | `--help` | affiche l'aide du programme | — |

- La génération initiale porte le numéro `0` : `-m 20` produit 21 générations.
- Lorsqu'une grille est fournie sur l'entrée standard, `--nb_cells` et `--seed` sont ignorés.
- En sortie `image`, les fichiers sont nommés `grid_XXXX.png` (numéro sur quatre chiffres).
- En sortie `text`, rien n'est écrit sur le disque : seule la dernière itération est affichée sur `STDOUT`.

## Vidéos

### Simulation du jeu de la vie

Lien YouTube : **[À COMPLÉTER](https://www.youtube.com/)**

Grille de 50 × 50, **graine `4200`**, 2001 générations (0 à 2000), conditions aux limites fixes, 20 images par seconde.

Commandes exactes, à lancer depuis la racine du dépôt dans un terminal sans pipe ni redirection :

```bash
mkdir -p outputs/video-seed-4200
python3 main.py --nb_cells 50 --max_iterations 2000 --seed 4200 \
  --output_type image --output_directory outputs/video-seed-4200
ffmpeg -y -framerate 20 -start_number 0 \
  -i outputs/video-seed-4200/grid_%04d.png -frames:v 2001 \
  -c:v libx264 -pix_fmt yuv420p -movflags +faststart \
  outputs/video-seed-4200/game-of-life.mp4
```

### Historique du dépôt avec Gource

Lien YouTube : **[À COMPLÉTER](https://www.youtube.com/)**

Commande utilisée, depuis la racine du dépôt :

```bash
gource -s 2 -r 60 --file-font-size 8 \
  --title 'Jeu de la vie' --filename-time 2 \
  --stop-at-end --hide date,usernames -o - | \
ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - \
  -vcodec libx264 -preset medium -pix_fmt yuv420p \
  -crf 18 -threads 0 -bf 0 gource.mp4
```

Les images et vidéos générées (`*.png`, `*.mp4`, `gource.ppm`) sont exclues de Git par le `.gitignore`.

## Auteurs

| Nom | Prénom | Numéro étudiant |
|---|---|---|
| MAILLOT CADET | Enzo Amable | À COMPLÉTER |
| BOYER | John-Lucas | À COMPLÉTER |
| PAYET | Arthur | À COMPLÉTER |
| POUNIANDY | Rajan | À COMPLÉTER |
| RAVALISON RABOANA | Jérémie | À COMPLÉTER |

## Liens utiles

- [Sujet du projet](README-consigne.md) : consignes et barème de l'évaluation,
- [Jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) : présentation des règles du jeu de Conway,
- [Documentation argparse](https://docs.python.org/fr/3/library/argparse.html) : analyse des arguments d'un script Python,
- [Documentation random](https://docs.python.org/fr/3/library/random.html) : génération de grilles aléatoires reproductibles,
- [Documentation sys](https://docs.python.org/fr/3/library/sys.html) : lecture de `STDIN` et écriture sur `STDERR`,
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix)) : description du pipe,
- [Bien nommer ses commits](https://buzut.net/cours/versioning-avec-git/bien-nommer-ses-commits) : conventions des messages de commit,
- [Documentation officielle de git rebase](https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Rebaser-Rebasing) : fonctionnement du *rebase*,
- [Workshop 3 : rebase et historique final](https://github.com/frozar/git-workshop-3) : organisation Git attendue pour ce projet,
- [Documentation ffmpeg](https://ffmpeg.org/documentation.html) : installation et utilisation de `ffmpeg`,
- [Site officiel de Gource](https://gource.io/) : présentation et téléchargement de Gource,
- [Installation de WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) : procédure officielle pour Windows.
