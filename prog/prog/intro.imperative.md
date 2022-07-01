## Exemple de paradigme : l'impératif

* Brique élémentaire : l'**instruction**

* Idée générale :
  - la machine possède un **état** (mémoire, registres, &hellip;),
  - chaque instruction modifie cet état,
  - les instructions se composent en **séquence**.

* Représentants historiques : Fortran (1954), Algol (1958)

* Exemple emblématique : **C** (1972, dernière norme : 2018)

--

## Cas d'étude : la suite de Fibonacci

- Un objet mathématique simple à définir&nbsp;:

$$
\begin{cases}
f_0 = 1 \\\\
f_1 = 1 \\\\
f_{n} = f_{n-1} + f_{n-2} \quad \textrm{si}~n \geq 2
\end{cases}
$$

$$ 1, 1, 2, 3, 5, 8, 13, 21, 34 \ldots $$

- Un programme simple à spécifier&nbsp;:

```python
def fibo(n):
	"""Assuming that n is a non-negative integer (i.e n >= 0)
	   Returns the n-th element of the Fibonacci sequence """
```
<!-- .element: style="padding:10px; background-color: #3f3f3f; font-size: 24px" -->

- Plusieurs exemples tirés de [Rosetta Code](http://rosettacode.org).


--

## Code impératif : Assembleur

Calcul de la suite de Fibonacci en Assembleur 8080 <!-- .element: class="title" -->

```x86asm
fibnci: mov  C,  A  ; C will store the counter
        dcr  C      ; decrement because we know f(1) already
        mvi  A,  1
        mvi  B,  0
loop:   mov  D,  A
        add  B      ; A := A + B
        mov  B,  D
        dcr  C
        jnz  loop   ; jump if not zero
        ret         ; return from subroutine
```
<!-- .element: style="font-size: 24px" -->

https://rosettacode.org/wiki/Fibonacci_sequence#8080_Assembly <!-- .element: class="small" -->

--

## Code impératif : Fortran

Calcul de la suite de Fibonacci en Fortran IV (1962)<!-- .element: class="title" -->

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
<!-- .element: style="font-size: 20px" -->

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
<!-- .element: style="font-size: 24px" -->

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
<!-- .element: style="font-size: 24px" class: "large" -->

</div>

--
## Flot de contrôle

- La programmation structurée encourage l'utilisation de **structures
  de contrôle** pour organiser le code :

  * branchements (<span class="label">Python</span> `if`),
  * boucles (<span class="label">Python</span> `for`, `while`),
  * blocs de code (`begin`, `end`).

- &hellip; et leur arrangement à discrétion dans des fonctions.

- L'idée est d'organiser le **flot de contrôle**, à savoir
  l'agencement des instructions entre elles.

  * problème des sauts (`goto`, jumps)

--
## Graphe de flot de contrôle

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

- Pour structurer ces ensembles d'instructions, il est naturel
  d'arranger le code en ensembles de fonctions.

- Cet arrangement est une première forme d'organisation
  **hiérarchique** du code.

- La généralisation de cette idée est la notion d'**architecture
  logicielle** : un ensemble de modèles et techniques pour organiser
  des composants logiciels de manière efficace.

- Exemple&nbsp;: la **programmation modulaire**.
