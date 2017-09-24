# Exercise 81: Compute the Hypotenuse

Fra side 39 i __Stevensons__ _The Python Workbook_

> Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. Include a main program that reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of the hypotenuse, and displays the result.

![Den retvinklede trekant](http://media.studieportalen.dk/images/cmspages/figur1hypotenusen.svg)

Skriv en funktion (f.eks. `hypotenuse` i filen `hypotenuse.py`). Funktionen skal tage længden af siderne i en retvinklet trekant, som parametre. Hvis du vil kan du kalde dem `a` og `b`. Returner hypotenusen (altså den lange side der ligger modsat den rette vinkel) i trekanten, beregnet efter Pythagoras læresætning, som funktionens resultat.

Pythagoras lærestning siger at: ![Pythagoras læresætning](http://media.studieportalen.dk/files/webbooks/images/65/equations/pWo4TXdA19G6_ffWivvEQQ==.gif)

Hvis vi tager kvadratroden på begge sider af lighedstegnet, kan hypotenusen beregnes med: 

![hypotenusen isoleret](http://media.studieportalen.dk/files/webbooks/images/65/equations/5efNKrB8yN0F2K8AucIdTw==.gif)

Lav også en `main()` funktion, 
* som beder brugeren indtaste længden af de korte sider (kateterne) i en retvinklet trekant (f.eks. 3 og 4),
* bruger din funktion til at beregne hypotenusen 
* og udskriver resultatet. 