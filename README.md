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
La description des options disponibles sur votre programme ;
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
