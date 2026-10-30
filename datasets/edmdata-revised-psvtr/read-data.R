e <- new.env()
load('original/items_revised_psvtr.rda', envir=e)
x <- e[['items_revised_psvtr']]
stopifnot(identical(dim(x), c(516L, 30L)), all(x %in% c(0, 1)), !anyNA(x))
print(dim(x))
