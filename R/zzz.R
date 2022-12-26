tdf <- NULL

.onLoad <- function(libname, pkgname) {
  tdf <<- reticulate::import_from_path(
    "tidydrfrost",
    system.file("assets/python", package = "tidydrfrost"),
    delay_load = TRUE
  )
}
