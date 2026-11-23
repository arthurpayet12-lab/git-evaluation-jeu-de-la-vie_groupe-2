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

## Exécution : 
- Plusieurs exemples d'utilisation de votre programme et les sorties attendues, comme ce qui est fait dans ce document ;

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
Les liens YouTube vers les deux vidéos publiques à produire :
  - au moins une vidéo de simulation du jeu de la vie produite avec votre programme `main.py`, à générer et publier à la fin de la partie implémentation du projet. Indiquez les commandes exactes de génération des images et de la vidéo, ainsi que la graine effectivement utilisée ;
  - une vidéo Gource représentant l'évolution de votre dépôt et reflétant un véritable travail de groupe ;
## Auteurs : 
    - RAVALISON Jeremie  45001523
    - POUNIANDY Rajan  45002281
    - PAYET Arthur  45003625
    - BOYER John-Lucas  46008228
    - MAILLOT-CADET Enzo  45001188
## Liens utiles
  - : Une liste de ressources en ligne qui vous a été utile pour réaliser ce projet. Cette liste doit être sous la même forme que la section [Liens utiles](#liens-utiles) de ce document.
