#' Complete Dr Frost Maths tasks
#' 
#' Complete a set of [Dr Frost Maths](https://www.drfrostmaths.com/) tasks. Each
#' task rewards the user with a certain number of points, which can vary.
#' 
#' @param tasks The tasks to complete. Either a [dr_frost_tasks()] object, or
#'   a character vector. If a character vector is supplied, it will be passed 
#'   as the `include` argument into the [dr_frost_tasks()] function. By default,
#'   all available tasks are completed.
#' @param email Used to login to the website. If `NULL`, the default email is 
#'   used.
#' @param password Used to login to the website. If `NULL`, the function will
#'   try to find the password corresponding to the `email` that has been set
#'   using [dr_frost_account()].
#' @param keyring A string, passed into [keyring::key_get()]. Use this if your 
#'   Dr Frost credentials are stored on a keyring that is not the default.
#' @param end Whether the browser session should be closed when the tasks are
#'   completed.
#' 
#' @details 
#' Completing Dr Frost Tasks requires a continuous (although not necessarily
#' fast) internet connection, and tasks will fail if no connection is found for
#' an extended period of time.
#'  
#' Completing each task calls a corresponding function in Python. 
#' 
#' @returns 
#' A data frame of information about each task, with 4 variables:
#' \describe{
#'   \item{task}{The task that was attempted.}
#'   \item{completed}{Whether the task was successfully completed.}
#'   \item{points}{The number of points that were earned by completing the task.}
#'   \item{error}{If the task failed, the error object that was returned.}
#' }
#' 
#' @seealso 
#' * [dr_frost_account()] to store your account details securely.
#' * [install_selene()] to install python dependencies.
#' 
#' @examples 
#' \dontrun{
#'   perform_tasks("addition")
#'   perform_tasks()
#' }
#' 
#' @export
perform_tasks <- function(tasks = dr_frost_tasks(), email = NULL, 
                          password = NULL, keyring = NULL, end = TRUE) {
  tasks <- get_tasks(tasks)
  if(is.null(tasks)) {
    cli::cli_alert_info("No tasks specified.")
    return(result_init)
  }
  
  driver_setup(email, password, keyring)
  
  setup_javascript(tasks)
  
  cli::cli_alert_info("Beginning tasks.")
  
  results <- lapply(tasks, perform_task)
  results_df <- vctrs::vec_rbind(result_init,!!!results)
  
  if(!any(results_df$completed)) {
    cli::cli_alert_danger("All tasks failed.")
  } else {
    total_points <- sum(results_df$points, na.rm = TRUE)
    cli::cli_alert_success("Tasks finished.")
    cli::cli_alert_success("Total points: {.val {total_points}}.")
  }
  
  if(end) {
    try(tdf$driver_utils$end_session())
  }
  
  invisible(results_df)
}

perform_task <- function(task) {
  cli::cli_alert_info("Task: {.val {task}}.")
  points <- NA
  error <- NA
  
  if(task %in% c("fixed_time", "individual_practice")) {
    res <- switch(
      task,
      fixed_time = fixed_time(),
      individual_practice = individual_practice()
    )
    
    completed <- res$completed
    points <- res$points
    error <- res$error
    if(!completed) {
      res <- data.frame(
        task = task,
        completed = FALSE,
        points = NA
      )
      res$error <- list(error)
      return(res)
    } else {
      return(data.frame(
        task = task,
        completed = TRUE,
        points = points,
        error = NA
      ))
    }
  }
  
  error <- rlang::try_fetch({
    switch(
      task,
      continue_sequence = tdf$Algebra$Sequences$continue_sequence(),
      later_terms = tdf$Algebra$Sequences$later_terms(),
      simple_substitution = tdf$Algebra$Solving_Equations$simple_substitution(),
      solve_one_step = tdf$Algebra$Solving_Equations$solve_one_step(),
      mean = tdf$Data_Handling_and_Probability$Averages_and_Range$mean(),
      pictograms = tdf$Data_Handling_and_Probability$Data_Representation$pictograms(),
      bar_charts = tdf$Data_Handling_and_Probability$Data_Representation$bar_charts(),
      bank_statements = tdf$Data_Handling_and_Probability$Data_Representation$bank_statements(),
      pie_charts = tdf$Data_Handling_and_Probability$Data_Representation$pie_charts(),
      addition_subtraction = tdf$Number$Arithmetic_Operations$addition_subtraction(),
      multiplication = tdf$Number$Arithmetic_Operations$multiplication(),
      pictoral_division = tdf$Number$Arithmetic_Operations$pictoral_division(),
      division = tdf$Number$Arithmetic_Operations$division(),
      number_facts = tdf$Number$Arithmetic_Operations$number_facts(),
      missing_digits = tdf$Number$Arithmetic_Operations$missing_digits(),
      bidmas = tdf$Number$Arithmetic_Operations$bidmas(),
      estimate_calculations = tdf$Number$Arithmetic_Operations$estimate_calculations(),
      place_value = tdf$Number$Decimals$place_value(),
      decimal_addition_subtraction = tdf$Number$Decimals$decimal_addition_subtraction(),
      conversion = tdf$Number$Fraction_Decimal_and_Percentage_Correspondences$conversion(),
      shape_fractions = tdf$Number$Fractions$shape_fractions(),
      equivalent_fractions = tdf$Number$Fractions$equivalent_fractions(),
      fraction_integer_division = tdf$Number$Fractions$fraction_integer_division(),
      order_fractions = tdf$Number$Fractions$order_fractions(),
      {cli::cli_abort("Task not found: {.val {task}}.")}
    )
    cli::cli_alert_success("Task completed.")
    NA
  }#, error = function(c) {
  #  cli::cli_alert_danger("Task failed.")
  #  c
  #}
  )
  
  if(all(is.na(error))) {
    error <- rlang::try_fetch({
      points <- tdf$driver_utils$get_points()
      cli::cli_alert_success("Points obtained: {.val {points}}.")
      NA
    }, error = function(c) {
      cli::cli_alert_danger("Could not get points.")
      c
    })
  }
  
  if(is.na(points)) {
    res <- data.frame(
      task = task,
      completed = FALSE,
      points = NA
    )
    res$error <- list(error)
    res
  } else {
    data.frame(
      task = task,
      completed = TRUE,
      points = points,
      error = NA
    )
  }
}

setup_javascript <- function(tasks) {
  print(tasks)
  table <- dr_frost_tasks(tasks)
  topic <- format_names(table$topic)
  subtopic <- format_names(table$subtopic)
  files <- get_js_files(topic, subtopic)
  lapply(files, source_js)
  print(files)
}

format_names <- function(x) {
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
