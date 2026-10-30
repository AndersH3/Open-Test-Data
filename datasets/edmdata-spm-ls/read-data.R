e <- new.env()
load('original/items_spm_ls.rda', envir=e)
x <- e[['items_spm_ls']]
stopifnot(identical(dim(x), c(499L, 12L)), all(x %in% c(0, 1)), !anyNA(x))
print(dim(x))
