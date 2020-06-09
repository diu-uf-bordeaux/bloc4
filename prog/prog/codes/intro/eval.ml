let i = ref 0;;

let f() =
  i := !i + 1;
  !i;;

let _ =
  Printf.printf "%d\n" (f() - f());;
