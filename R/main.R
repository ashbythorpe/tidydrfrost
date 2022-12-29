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
    tdf$driver_utils$end_session()
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

error <- NA
rlang::try_fetch({
  error <- 1
})
error
