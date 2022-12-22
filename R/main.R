perform_tasks <- function(tasks = dr_frost_tasks(), email = NULL, 
                          password = NULL, keyring = NULL, end = TRUE) {
  tasks <- get_tasks(tasks)
  if(is.null(tasks)) {
    cli::cli_alert_info("No tasks specified.")
    return(result_init)
  }
  
  driver <- driver_setup(email, password, keyring)
  
  cli::cli_alert_info("Beginning tasks.")
  
  results <- lapply(tasks, perform_task, driver = driver)
  results_df <- vctrs::vec_rbind(result_init,!!!results)
  
  if(!any(results_df$completed)) {
    cli::cli_alert_danger("All tasks failed.")
  } else {
    total_points <- sum(results_df$points, na.rm = TRUE)
    cli::cli_alert_success("Tasks finished.")
    cli::cli_alert_success("Total points: {.val {total_points}}.")
  }
  
  if(end) {
    tdf$driver_utils$end_session(driver)
  }
  
  invisible(results_df)
}

perform_task <- function(task, driver) {
  cli::cli_alert_info("Task: {.val {task}}.")
  points <- NA
  error <- NA
  
  error <- try({
    switch(
      task,
      addition_subtraction = tdf$KS3$Number$addition_subtraction(driver),
      multiplication = tdf$KS3$Number$multiplication(driver),
      pictoral_division = tdf$KS3$Number$pictoral_division(driver),
      division = tdf$KS3$Number$division(driver)
    )
    points <- reticulate::py_to_r(tdf$utils$get_points(driver))
    cli::cli_alert_success("Task completed.")
    cli::cli_alert_success("Points obtained: {.val {points}}.")
  }, silent = TRUE)
  
  if(is.na(points)) {
    cli::cli_alert_danger("Task failed.")
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
