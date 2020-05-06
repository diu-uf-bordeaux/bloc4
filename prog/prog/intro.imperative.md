## Exemple de paradigme : l'impératif

* Brique élémentaire : l'**instruction**

* Idée générale :
  - la machine possède un **état** (mémoire, registres, &hellip;)
  - chaque instruction modifie cet état

* Les instructions se composent en **séquence**.

* Historique ? (Fortran, Algol)

Exemple (genre exemple récurrent, ou sur un thème proche)

Exemple classique (genre en C)

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

https://rosettacode.org/wiki/Fibonacci_sequence

--

## Code impératif : Python

- Routine de calcul de la suite de Fibonacci

```python
def fibo(n):
	if n <= 1
        return 1
    else:
	    a = 0
		b = 1
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
```

--

## Paradigme modulaire

Transition avec l'impératif, les procédures, puis les modules.

Parler d'architecture quelque part.

--

## Autres paradigmes

Paradigme logique (cf. logpy)

Paradigme parallèle

Paradigme événementiel
