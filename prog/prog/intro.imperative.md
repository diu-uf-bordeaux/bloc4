## Exemple de paradigme : l'impératif

* Brique élémentaire : l'**instruction**

* Idée générale :
  - la machine possède un **état** (mémoire, registres, &hellip;)
  - chaque instruction modifie cet état

* Les instructions se composent en **séquence**.

* Représentants historiques : Fortran (1954), Algol (1958)

* Exemple actuel : **C** (1972, dernière norme : 2018)

--

## Code impératif : Assembleur

- Routine de calcul de la suite de Fibonacci

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

- Fonction de calcul de la suite de Fibonacci

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

- Fonction de calcul de la suite de Fibonacci

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

- Fonction de calcul de la suite de Fibonacci

```python
def fibo(n):
    if n <= 1:
        return n
    fibPrev = 1
    fib = 1
    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib
```
