#' Install the selene python package
#' 
#' tidydrfrost depends on the 'selene' python package. This function resolves
#' this dependency.
#' 
#' @param method,conda Passed into [reticulate::py_install()]
#' 
#' @examples 
#' \dontrun{
#'   install_selene()
#' }
#'
#' @export
install_selene <- function(method = "auto", conda = "auto") {
  reticulate::py_install("selene", method = method, conda = conda)
}
