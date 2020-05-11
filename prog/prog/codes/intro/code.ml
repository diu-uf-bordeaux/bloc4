module Sequence = struct
   let fibo(n) =
     let fibP = ref (0,1) in
     for i = 1 to n do
           let (u,v) = !fibP in
           fibP := (v, u+v)
     done;
     fst !fibPr

  let rec range (a,b) =
    if (a >= b) then [] else a :: range(a+1,b)

  let choose(n, r) =
    let r = min r (n-r) in
    if r = 0
    then 1
    else let num = List.fold_left ( * ) 1 (List.rev (range (n-r+1, n+1)))
         and den = List.fold_left ( * ) 1 (range(1, r+1))
         in num / den

  let catalan n = choose(2*n, n) / (n+1)


end;;

module SequenceTest = struct
  open Sequence

  let list_equal l1 l2 =
    List.fold_left2 (fun acc e1 e2 -> acc && (e1 == e2)) true l1 l2

  let test_fibo () =
    let tab1 = [0; 1; 1; 2; 3; 5; 8; 13; 21; 34]
    and tab2 = List.map fibo (range (0,10))
    in list_equal tab1 tab2

  let test_catalan () =
    let tab1 = [1; 1; 2; 5; 14; 42; 132; 429; 1430; 4862]
    and tab2 = List.map catalan (range (0,10))
    in list_equal tab1 tab2

end;;

SequenceTest.test_fibo();;
