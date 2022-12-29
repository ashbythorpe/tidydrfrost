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
      addition_subtraction = tdf$KS2_Number$Arithmetic_Operations$addition_subtraction(),
      multiplication = tdf$KS2_Number$Arithmetic_Operations$multiplication(),
      pictoral_division = tdf$KS2_Number$Arithmetic_Operations$pictoral_division(),
      division = tdf$KS2_Number$Arithmetic_Operations$division(),
      number_facts = tdf$KS2_Number$Arithmetic_Operations$number_facts(),
      missing_digits = tdf$KS2_Number$Arithmetic_Operations$missing_digits(),
      bidmas = tdf$KS2_Number$Arithmetic_Operations$bidmas(),
      estimate_calculations = tdf$KS2_Number$Arithmetic_Operations$estimate_calculations()
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
