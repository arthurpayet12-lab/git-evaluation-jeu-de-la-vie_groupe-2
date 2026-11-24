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

## Exécution

Voici plusieurs exemples d'utilisation de notre programme illustrant les différents modes de fonctionnement et les sorties attendues.

### 1. Simulation par défaut (génération d'images)

Sans aucun argument, le programme utilise les valeurs par défaut (grille aléatoire de 10x10, 20 itérations, graine 42) et génère **21 images PNG** dans le dossier `outputs/` :

```bash
python3 main.py
```

**Sortie console attendue :**
```text
Generation of 21 images in directory outputs
```

### 2. Simulation avec paramètres personnalisés

Pour générer 201 images (de `grid_0000.png` à `grid_0200.png`) avec une grille de 50 cellules par côté et une graine fixée à `4200` :

```bash
python3 main.py -n 50 -m 200 -s 4200
```

**Sortie console attendue :**
```text
Generation of 201 images in directory outputs
```

### 3. Évolution d'une grille lue sur l'entrée standard (STDIN) en mode texte

En fournissant une grille via un pipe Unix avec `-t text`, aucune image n'est créée : seule la dernière génération demandée est affichée sur la sortie standard (`STDOUT`).

Exemple pour calculer 1 itération avec les conditions aux limites fixes (par défaut) :

```bash
cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
```

**Sortie console attendue :**
```text
iteration: 1
0 1 0
0 0 1
0 1 0
```

### 4. Grille avec conditions aux limites périodiques (`-p`)

L'option `-p` ou `--periodic` replie la grille sur elle-même (forme de tore). Pour la même grille que ci-dessus, le résultat est différent :

```bash
cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
```

**Sortie console attendue :**
```text
iteration: 1
0 0 0
0 0 0
0 0 0
```

### 5. Lancement des tests automatiques

Pour vérifier la conformité des options de la ligne de commande et la validité algorithmique du jeu :

```bash
sh check_script_options.sh
sh check_tests.sh
```

## Arguments : 

Le programme `main.py` accepte plusieurs options en ligne de commande, disponibles sous leur forme courte et longue :

| Option courte | Option longue | Type / Valeurs | Description | Valeur par défaut |
| :--- | :--- | :--- | :--- | :--- |
| `-n N` | `--nb_cells N` | Entier (N>0) | Nombre de cellules par côté pour une grille aléatoire | `10` |
| `-m N` | `--max_iterations N` | Entier (N0) | Numéro de la dernière itération à calculer | `20` |
| `-s N` | `--seed N` | Entier | Graine du générateur de nombres aléatoires | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | Chemin | Dossier dans lequel écrire les images générées | `outputs` |
| `-t TYPE` | `--output_type TYPE` | `image` ou `text` | Type de sortie produit par le programme | `image` |
| `-p` | `--periodic` | Drapeau (*flag*) | Active les conditions aux limites périodiques (grille torique) | Désactivée |
| `-h` | `--help` | — | Affiche le message d'aide et quitte le programme | — |

### Détails et contraintes des paramètres

- **Taille de la grille (`-n`, `--nb_cells`)** : Doit être un entier strictement positif. Cette option définit la taille de la matrice carrée générée aléatoirement. Elle est ignorée si une grille est fournie sur l'entrée standard (`STDIN`).
- **Nombre d'itérations (`-m`, `--max_iterations`)** : Doit être un entier positif ou nul. La génération initiale porte le numéro `0`. Par conséquent, une simulation avec `-m 20` calcule et produit **21 générations** (de `0` à `20` incluses).
- **Graine aléatoire (`-s`, `--seed`)** : Accepte tout entier relatif (positif, négatif ou nul). À taille et graine identiques, le générateur produit une grille initiale strictement reproductible. Cette option est ignorée si une grille est lue depuis `STDIN`.
- **Dossier de sortie (`-o`, `--output_directory`)** : Chemin du dossier de destination des fichiers PNG. S'il n'existe pas, il est automatiquement créé.
- **Type de sortie (`-t`, `--output_type`)** :
  - `image` : Génère un fichier PNG par génération (de `grid_0000.png` à `grid_XXXX.png`).
  - `text` : Ne génère aucune image. Affiche uniquement la dernière itération demandée sur la sortie standard (`STDOUT`) au format textuel `iteration: N` suivi de la grille de `0` et `1`.
- **Conditions aux limites périodiques (`-p`, `--periodic`)** : 
  - *Par défaut (sans `-p`)* : Conditions fixes ; toute cellule située en dehors de la grille est considérée comme morte.
  - *Avec `-p`* : La grille se replie sur elle-même (surface d'un tore) : le bord gauche est adjacent au bord droit, et le bord supérieur au bord inférieur.
- **Aide en ligne (`-h`, `--help`)** : Affiche la documentation d'utilisation générée automatiquement par `argparse`.



## Vidéos : 
Les liens YouTube vers les deux vidéos :
  - [Simulation du jeu de la vie](https://youtu.be/ELl9sex1T-c?si=cgpLcRMOoOI2xNSa)
  - une vidéo Gource représentant l'évolution de votre dépôt et reflétant un véritable travail de groupe ;
## Auteurs : 
    - RAVALISON Jeremie  45001523
    - POUNIANDY Rajan  45002281
    - PAYET Arthur  45003625
    - BOYER John-Lucas  46008228
    - MAILLOT-CADET Enzo  45001188
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
