#include <stdio.h>

int i = 0;

int f() {
  i++;
  return i;
}

int sub(int x, int y) { return x - y; }

int main(void) {
  printf("%d\n", sub(f(),f()));
}

// Compile with clang or gcc to get different results
