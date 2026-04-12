# ShowTimer

**ShowTimer** est un logiciel de gestion de minutage et de cues pour la tv / spectacle. Il permet à l'opérateur de suivre le déroulement d'un show en temps réel, de déclencher des cues automatiquement, d'afficher un prompteur sur un écran secondaire et d'envoyer des commandes OSC vers d'autres équipements.

---

## Captures d'écran

<img width="525" height="606" alt="image" src="https://github.com/user-attachments/assets/c20a8ee4-dcbd-4db9-9ca4-d57546928df9" />
<img width="1277" height="894" alt="image" src="https://github.com/user-attachments/assets/99b5874e-35ac-497d-b7a8-15fcf1ecef31" />




---

## Fonctionnalités

### Gestion des shows
- Création, modification et suppression d'émissions
- Sélection de l'émission active parmi une liste
- Durée totale configurable par émission

### Gestion des cues
- Ajout, modification et suppression de cues
- Chaque cue possède un titre, une description, un temps de déclenchement, une couleur et une commande OSC optionnelle
- Import depuis un fichier **CSV** ou **Excel** (.xlsx)
- Export en **CSV**, **Excel** et **PDF** 

### Minutage en temps réel
- Timer principal avec démarrage, pause et reset
- Suivi automatique des cues : le cue courant est mis en évidence, les cues passés sont grisés
- Alertes visuelles par clignotement selon le temps restant avant le prochain cue :
  - **Vert** à 15 secondes
  - **Orange** à 10 secondes
  - **Rouge** à 5 secondes

### Prompteur
- Fenêtre dédiée affichable sur un écran secondaire
- Affiche le titre du cue en cours, le suivant et le second suivant
- Horloge temps réel intégrée
- Personnalisation complète : taille et couleur de chaque zone, largeur des contours, seuils et couleurs des alertes de clignotement

### OSC
- Envoi de commandes OSC à l'adresse IP et au port configurés
- Activation / désactivation de l'OSC depuis l'interface

### Sécurité
- Verrouillage de l'interface opérateur par mot de passe
- Mot de passe stocké dans un fichier `.stpass` (modifiable manuellement)
- Mot de passe par défaut : `admin`

### Logs
- Journalisation complète de la session dans un fichier horodaté (`logs/session_YYYY-MM-DD_HH-MM-SS.txt`)
- Affichage en temps réel des logs dans l'interface opérateur
- Accès rapide au dossier de logs et possibilité de les supprimer depuis l'interface

---

## Installation

### Depuis l'installateur (recommandé)

1. Téléchargez le fichier `ShowTimer_1.0_setup.exe` depuis la page [Releases](../../releases).
2. Lancez l'installateur et suivez les étapes.
3. Un raccourci est créé sur le bureau et dans le menu Démarrer.
4. Les données utilisateur (base de données, logs, mot de passe) sont stockées dans :
   ```
   C:\Users\<Utilisateur>\AppData\Local\Foxx Production\ShowTimer\
   ```

### Depuis les sources

**Prérequis :**
- Python 3.11+
- Les dépendances listées dans `requirements.txt`

```bash
git clone https://github.com/Foxxprod/ShowTimer.git
cd ShowTimer
pip install -r requirements.txt
python main.py
```

---


## Utilisation

### Premier lancement
Au premier lancement, la base de données et le fichier `.stpass` sont créés automatiquement. Le mot de passe par défaut est `admin`.

### Créer un show
1. Aller dans l'onglet **Shows**
2. Cliquer sur **Ajouter** et renseigner le nom, la description et la durée totale
3. Sélectionner le show dans la liste pour l'activer

### Ajouter des cues
1. Avec le show actif sélectionné, aller dans l'onglet **Cues**
2. Cliquer sur **Ajouter un cue**
3. Renseigner le titre, la description, le temps de déclenchement et optionnellement une commande OSC
4. Valider avec **Entrée** ou le bouton **Enregistrer**

### Importer des cues
- Cliquer sur **Importer CSV** ou **Importer Excel** / Creer des cues manuellement.
- Les cellules avec des valeurs manquantes ou un temps à zéro sont surlignées en rouge dans l'aperçu
- Confirmer pour importer

### Lancer le timer
1. Appuyer sur **Démarrer**
2. Le cue courant est mis en évidence en vert dans la liste
3. Les cues passés apparaissent en gris, le suivant en vert foncé
4. Les alertes de clignotement s'activent automatiquement selon le temps restant

### Afficher le prompteur
1. Cliquer sur **Ouvrir le prompteur**
2. Déplacer la fenêtre sur l'écran secondaire
3. La configuration (tailles, couleurs, seuils) est accessible depuis l'onglet **Prompteur**

### Exporter le show
- **PDF** : cliquer sur le bouton d'export PDF — génère un rapport complet du show
- **Excel / CSV** : cliquer sur le bouton correspondant — fichier exporté dans le dossier courant

---

## Configuration requise

| Élément | Minimum |
|---|---|
| OS | Windows 10 64-bit |
| RAM | 2 Go |
| Résolution | 1280 × 720 |
| Espace disque | 100 Mo |

---

## Licence

Ce logiciel est la propriété exclusive de **Foxx Production**. Toute reproduction, distribution ou modification sans autorisation écrite est interdite. Voir [LICENSE.txt](LICENSE.txt) pour le texte complet.

---

© 2026 Foxx Production — [foxxprod.fr](https://www.foxxprod.fr/)
