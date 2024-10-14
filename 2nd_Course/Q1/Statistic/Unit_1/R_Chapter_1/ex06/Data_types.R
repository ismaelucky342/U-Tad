x <- 3.14
class(x) # [1] "numeric"

y <- 5L
class(y) # [1] "integer"

is.numeric(5L) # [1] TRUE
is.integer(5) # [1] FALSE

x <- -1/0
is.infinite(x) # [1] TRUE

y <- 0/0
class(y) # [1] "numeric"
is.nan(y) # [1] TRUE

x <- TRUE
class(x) # [1] "logical"

y <- "Hola Mundo"
class(y) # [1] "character"

f <- NA
is.na(f) # [1] TRUE

x <- "2.14"
y <- as.numeric(x) 
y + 1 # [1] 3.14

z <- "Hola"
as.numeric(z) # Warning: NAs introduced by coercion [1] NA
