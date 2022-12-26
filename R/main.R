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
  
  rlang::try_fetch({
    switch(
      task,
      addition_subtraction = tdf$KS3$Number$addition_subtraction(),
      multiplication = tdf$KS3$Number$multiplication(),
      pictoral_division = tdf$KS3$Number$pictoral_division(),
      division = tdf$KS3$Number$division()
    )
    cli::cli_alert_success("Task completed.")
  }, error = function(c) {
    error <- c
    cli::cli_alert_danger("Task failed.")
  })
  
  if(is.na(error)) {
    rlang::try_fetch({
      points <- tdf$driver_utils$get_points()
      cli::cli_alert_success("Points obtained: {.val {points}}.")
    }, error = function(c) {
      error <- c
      cli::cli_alert_danger("Could not get points.")
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
