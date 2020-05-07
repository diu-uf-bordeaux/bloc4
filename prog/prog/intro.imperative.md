## Exemple de paradigme : l'impératif

* Brique élémentaire : l'**instruction**

* Idée générale :
  - la machine possède un **état** (mémoire, registres, &hellip;)
  - chaque instruction modifie cet état
  - les instructions se composent en **séquence**

* Représentants historiques : Fortran (1954), Algol (1958)

* Exemple emblématique : **C** (1972, dernière norme : 2018)

--

## Code impératif : Assembleur

Calcul de la suite de Fibonacci en Assembleur 8080 <!-- .element: class="title" -->

```x86asm
fibnci: mov  C,  A  ; C will store the counter
        dcr  C      ; decrement, because we know f(1) already
        mvi  A,  1
        mvi  B,  0
loop:   mov  D,  A
        add  B      ; A := A + B
        mov  B,  D
        dcr  C
        jnz  loop   ; jump if not zero
        ret         ; return from subroutine
```

https://rosettacode.org/wiki/Fibonacci_sequence#8080_Assembly <!-- .element: class="small" -->

--

## Code impératif : Fortran

Calcul de la suite de Fibonacci en Fortran <!-- .element: class="title" -->

```fortran
      FUNCTION IFIBO(N)
      IF(N) 9,1,2            ; test N == 0
    1 IFN=0
      GOTO 9
    2 IF(N-1) 9,3,4          ; test N == 1
    3 IFN=1
      GOTO 9
    4 IFNM1=0
      IFN=1
      DO 5 I=2,N             ; start loop
      IFNM2=IFNM1
      IFNM1=IFN
    5 IFN=IFNM1+IFNM2        ; end loop
    9 IFIBO=IFN
      END
```

https://rosettacode.org/wiki/Fibonacci_sequence#FORTRAN_IV <!-- .element: class="small" -->

--

## Code impératif : C

Calcul de la suite de Fibonacci en C <!-- .element: class="title" -->

```c
long long int fibo(int n) {
	int fnow = 0, fnext = 1, tempf;
	while (--n > 0) {
		tempf = fnow + fnext;
		fnow = fnext;
		fnext = tempf;
	}
	return fnext;
}
```

https://rosettacode.org/wiki/Fibonacci_sequence#Iterative_13 <!-- .element: class="small" -->

--

## Code impératif : Python

<div>

Calcul de la suite de Fibonacci en Python <!-- .element: class="title" -->

```python
def fibo(n):
    if n <= 1:
        return n
    fibPr = 1
    fib = 1
    for num in range(2, n):
        fibPr, fib = fib, fib + fibPr
    return fib
```

</div>

--
## Transition vers le modulaire

- La programmation structurée encourage l'utilisation de **structures
  de contrôle** pour organiser le code :

  * branchements (<span class="label">Python</span> `if`)
  * boucles (<span class="label">Python</span> `for`, `while`)
  * blocs de code

- &hellip; et leur arrangement à discrétion dans des fonctions.

- L'idée est de structurer le **flot de contrôle**, à savoir
  l'agencement des instructions entre elles.

  * problème des sauts (`goto`, jumps)

--
## Graphe de flot contrôle

<div class='half'>

en Python  <!-- .element: class="title" -->
```python
def fibo(n):
    if n <= 1:
        return n
    fibPr = 1
    fib = 1
    for num in range(2, n):
        fibPr, fib = fib, fib + fibPr
    return fib
```
</div>
<div class='half'>

![Graphe de flot de contrôle](prog/images/intro/cfg.png)

</div>

--
## Transition vers le modulaire


- L'arrangement du code en fonctions est une première forme
  d'organisation **hiérarchique** du code.

- La généralisation de cette idée est la notion d'**architecture
  logicielle** : un ensemble de modèles et techniques pour organiser
  des composants logiciels de manière efficace.
