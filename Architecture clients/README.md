## Architecture clients/serveur 

## TP 3- Serveur TCP/IP SIMPLE a - Contexte

### Partie 2.1

Il peux avoir un probleme d'écriture de données en simultané (Trois personnes qui écrivent un fichier en meme temps) OU serveur - client (Une personne écrit dans un channel qui vient d'être supprimé) OU du serveur lui même (Boucle infini d'attente d'un utilisateur.). Une erreur peux survenir si un client rejoint et quitte en meme temps, par exemple en inversant les deux personnes. Bitre systèle est vulnérable aux problmes d'état, il suffrait d'essayer de prévoire les problemes avec des blocs try/catch (Le but étant de garder le serveur actif).

### Partie 2.2

Les responsabilités de notre application serveur, est de gerer des canaux de disscution/ messages. Il est donc nécessaire, que le traitement des données, la fiabilité des messages, les commandes clients. En cas d'erreur dans une commande, ça doit être la couche logique qui doit repondre. On peux séparer la logique métier et la logique d'entrée sortie.

### Partie 2.3

Si on doit rajouté une nouvelle commande, il faut changer la partie du serveur, s'occupant du traitement des commandes. Il ne faut également pas oublier de charger le /help. Il faudrait un service qui puis être localisé à plus grande échelles, et du multithreading des tâches. Le fait d'avoir tout les tâches sur la même machine empeche une bonne existance du service.

### Partie 2.4

Les modules candidats naturels serait les serveur d'enregistrement des requetes (log), qui serront parfait dans ce cas la. Le serveur en lui même, est un bloc monolithique, qui est bloqué dans un mode (reception de données).

### Partie 2.5

Le serveur peut être detecter une déconnexion brutale, dans le cas ou une méthode de trame de vie est installer. Si un message est pas reçu, vu qu'il s'agit d'un modele TCP, le serra (un jour, surment). Grâce à ceci, on peux garentir une livraison (SYN, SYN-ACK, ACK).

### Partie 2.6

Les regles implicites du protocole sont assez claires : "/" + commande (+ argument(s)). Il s'agit d'un protocole explicite, mais dans le cadre d'une méthode précise et écrite via un /help, cela devient un protocole documenté.

## Serveur TCP/IP PARTIE B

### Qui traite les commandes ?

LA fonction qui interprète /mag, /join, est la fonction handle, qui est appellé à chaque fois que le serveur réception un message.
TOut le monde a accès la mémoire partargée etat_serveur, ce qui montre un certain probleme de process au niveau du codage.

### Ou sont stockées les infos ?

Toutes les informations sont stocké dans la mémoire partagé etat_serveur.
Tous les fichiers wfile sont associé à chaque personne via leurs pseudonymes.

### Qui peut planter ?

Si une personne se deconnecte, le logiciel peux rester bloquer sur le serveur.
Si un write echoue, il y a rien de prévue. En effet, il y a juste un continue dans ce cadre la.
Dans la version actuelle les canaux ne peuvent pas être supprimer.