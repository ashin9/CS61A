(define (split-at lst n)
  ;(if (> n (length lst)) 
  ;  (cons lst nil)
  ;  (if (= n 1)
  ;    (cons (car lst) (cdr lst))
  ;    (cons (car lst) (split-at (cdr lst) (- n 1)))
  ;  )
  ;)

  (cond
    ((= n 0) (cons nil lst))
    ((null? lst) (cons lst nil))
    (else
      ; rec 是递归调用 (split-at (cdr lst) (- n 1)) 得到的分割结果
      (let ((rec (split-at (cdr lst) (- n 1))))
        ; car rec 是 lst 剩余部分的前 n-1 个元素, cdr rec 是 lst 剩余部分的剩余元素
        (cons (cons (car lst) (car rec)) (cdr rec))
      )
    )
  )
)


(define (compose-all funcs)
  (lambda (x)
    (if (null? funcs)
      x
      ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
)

