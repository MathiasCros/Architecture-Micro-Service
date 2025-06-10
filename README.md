### Etape 1
Le socket cote serveur est bloquante, à partir du moment au suel de ne reçoit pas de requetes.
Si le client essaye de se connecter avant que le serveur lui autorise, cela affiche une erreur de connection refusé (errno 111)
Listen() permet d'écouter un socket, alors que bind() permet de reserver le port, et de le garder jusqu'a qu'il soit fini.

### Etape 2

La boucle permet de repondre a plusieurs requetes jusqu'a la fin du programme.
Si on oublie de mettre fin, le client sera déconnecté du serveur, mais aura toujours le script executé.
Le serveur ne peux pas envoyer plusieurs réponses d'affilée du à son architecture.

### Etape 3

Le serveur peux mais reste actif après la déconnection client.
On peux recevoir plusieurs personnes grâce à la deuxiement boucle qui accepte des nouvelles arrivées.
Via ce programe il n'est pas possible de faire ceci en parallèle dans cette architecture.

### Etape 4

On s'assurer de ceci en vérifiant la réception du message, ce qui permet de passer envoyer en mode envoie.
Il est possible de rendre cette échange non bloquant, via multiples threads.
Le meuilleur façon de quitter le programme est que le client écrit la commande fin.

### Etape 5

Via l'utilisation d'eval(), il est possible de faire un accès au base de données.
Dans l'exception du serveur on peux envoyer l'erreur, au client pour fair eplanter le client et non pas, le serveur.

### Etape 6 

Structurer les messages permet de savoir quel traitement on doit donner a chaque élements.
