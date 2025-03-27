(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  ;(if (eq? nil pairs)
  ;  nil
  ;  (cons 
  ;    (cons (caar pairs) (zip (cdr pairs)))
  ;    (cons (cdar pairs) (zip (cdr pairs)))
  ;  )
  ;)

  (define (helper s first second)
    (if (null? s)
      (list first second)
      (helper 
        (cdr s) 
        (append first (list (caar s))) 
        (append second (list (car (cdar s))))
      )
    )
  )
  (helper pairs nil nil)
  )


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper s i)
    (if (eq? nil s)
      nil
      (cons (list i (car s)) (helper (cdr s) (+ i 1)))
    )
  )
  (helper s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond
    ((eq? nil list1)
      list2
    )
    ((eq? nil list2)
      list1
    )
    (else
      (if (comp (car list1) (car list2))
        (cons (car list1) (merge comp (cdr list1) list2))
        (cons (car list2) (merge comp list1 (cdr list2)))
      )
    )

  )
)
  ; 错误点: 没有控制好 if-else, 三个 if 是单独de, 都会执行, 最终返回值为最后一个 if, 或者使用 if 嵌套起来
  ;(if (eq? nil list1)
  ;  list2
  ;)
  ;(if (eq? nil list2)
  ;  list1
  ;)
  ;(if (comp (car list1) (car list2))
  ;  (cons 
  ;    (car list1) 
  ;    (merge comp (cdr list1) list2)
  ;  )
  ;  (cons
  ;    (car list2)
  ;    (merge comp list1 (cdr list2))
  ;  )
  ;)
  ;)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    ; and 判断使用错误, 应该 (and () ()), 判读顺序错误, 应该选判断是否为 nil 再比较
    ; (if (> (car s) (cadr s) and not (eq? nil cadr s))
    (cond
      ((eq? nil s)
        nil
      )
      ((= 1 (length s))
        (cons s nil)
      )
      (else
        (if (> (car s) (cadr s))
          ; 这里能想到
          (cons
            (list (car s))
            (nondecreaselist (cdr s))
          )
          ; 这如何构造?
          (cons
            (cons 
              (car s)
              ; s = (1 2 3 0 1 2), 递归 (nondecreaselist '(2 3 0 1 2))，返回 ((2 3) (0 1 2))
              ; 1 <= 2 所以合并
              ; 取递归返回结果的第一段
              (car (nondecreaselist (cdr s)))
            )
            ; 取递归返回结果的其余部分
            (cdr (nondecreaselist (cdr s)))
          )
        )
      )
    )
)
    ;(if (> (car s) (cadr s))
    ;  (cons 
    ;    (list (car s)) 
    ;    (nondecreaselist (cdr s))
    ;  )
    ;  (cons
    ;    ; 结构错误
    ;    (list (car s) (nondecreaselist (cdr s)))
    ;  )
    ;)
    ;)
    
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     ; BEGIN PROBLEM EC
     expr
     ; END PROBLEM EC
    )
    ((quoted? expr)
     ; BEGIN PROBLEM EC
     expr
     ; END PROBLEM EC
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM EC
       (cons form (cons params (map let-to-lambda body)))
       ; END PROBLEM EC
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM EC
       (define tmp (zip values))
       (append (cons (cons 'lambda (cons (car tmp) (map let-to-lambda body))) nil) (map let-to-lambda (cadr tmp)))
       ; END PROBLEM EC
     ))
    (else
     ; BEGIN PROBLEM EC
     (cons (car expr) (map let-to-lambda (cdr expr)))
     ; END PROBLEM EC
    )))
