setup_javascript <- function(tasks) {
  table <- dr_frost_tasks(tasks)
  topic <- format_names(table$topic)
  subtopic <- format_names(table$subtopic)
  files <- get_js_files(topic, subtopic)
  lapply(files, source_js)
}

format_names <- function(x) {
  x <- tolower(x)
  x <- gsub(" ", "_", x, fixed = TRUE)
  x <- gsub(",", "", x, fixed = TRUE)
  gsub("&", "and", x, fixed = TRUE)
}

get_js_files <- function(topic, subtopic) {
  paths <- paste0("assets/js/", topic, "/", subtopic, ".js")
  actual <- vapply(paths, system.file, character(1), package = "tidydrfrost")
  c(actual[actual != ""], system.file("assets/js/utils.js", package = "tidydrfrost"))
}

source_js <- function(file) {
  rlang::try_fetch({
    tdf$driver_utils$source_js(file)
  }, error = function(c) {
    cli::cli_abort("Could not source JavaScript dependencies.", parent = c)
  })
}
