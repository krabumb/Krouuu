# Krouuu

Langage de programmation Krouuu

Krouuu est un langage de programmation orienté objet.
Ce langage a été crée afin de programmer des fenêtres sur windows
et linux beaucoup plus facilement en travaillant directement sur une fenêtre de travail.
Des fonctions built-in s'occupe de gérer la fenêtre.


# Exemple de programme qui affiche "Hello World" dans une fenêtre de travail et dans la console

programme_fr.krouuu
```
$ '$' sont les délimiteurs de commentaire
$ un commentaire s'arrête à la fin de la ligne
$ les commentaires sont ignorés par le compilateur


$ création d'une fenêtre par défaut (titre : Krouuu, taille : 500x500)
start new window {

    $ écrit "Hello World" sur la fenêtre à x = 10% et y = 50%
    printToWindow(10%, 50%, "Hello World"); 

    $ écrit "Hello World 1" et 'Hello World 2' dans la console
    $ on peut utiliser "" ou '' pour les chaines de caractères
    print("Hello World 1");
    print('Hello World 2');
}

$ création d'une fenêtre customisée (titre : Nouveau titre, taille : 1000x500)
start new window(1000, 500, "Nouveau titre") {

    $ écrit "Hello World" sur la fenêtre à x = 300 et y = 250
    printToWindow(300, 250, "Hello World");

    $ écrit "Hello World" et l'adresse mémoire de la fenêtre dans la console
    print("Hello World from " + super);
}
```

# Comment utiliser le compilateur Krouuu ?

```WIP```



