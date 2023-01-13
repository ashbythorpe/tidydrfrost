#' Install Python dependencies for tidydrfrost
#' 
#' tidydrfrost depends on a few python packages. This function installs these
#' using [reticulate::py_install].
#' 
#' @param method,conda Passed into [reticulate::py_install()]
#' 
#' @details 
#' tidydrfrost currently depends on 'selene', 'sigfig', 'sympy' and 'latex2sympy2'.
#' For added control over the installation of these packages, use 
#' [reticulate::py_install()] directly:
#' ```
#' reticulate::py_install(c("selene", "sigfig", "sympy", "latex2sympy2"))
#' ```
#' Or use `pip`:
#' ```
#' pip install selene sigfig sympy latex2sympy2
#' ```
#' 
#' @examples 
#' \dontrun{
#'   install_tdf_dependencies()
#' }
#'
#' @export
install_tdf_dependencies <- function(method = "auto", conda = "auto") {
  reticulate::py_install(
    c("selene", "sigfig", "sympy", "latex2"), method = method, conda = conda
  )
}
