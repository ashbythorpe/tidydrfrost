install_selene <- function(method = "auto", conda = "auto") {
  reticulate::py_install("selene", method = method, conda = conda)
}
