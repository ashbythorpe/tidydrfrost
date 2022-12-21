perform_tasks <- function(tasks = dr_frost_tasks(), email = NULL, 
                          password = NULL, keyring = NULL, end = TRUE) {
  vctrs::vec_assert(tasks, character())
  if(length(tasks) == 0) {
    return()
  }
  tasks <- tasks[tasks %in% dr_frost_tasks()]
  if(length(tasks) == 0) {
    return()
  }
  
  driver <- driver_setup(email, password, keyring)
  
  cli::cli_alert_info("Beginning tasks.")
  
  purrr::walk(tasks, perform_task, driver = driver)
  
  cli::cli_alert_success("Tasks finished.")
  
  if(end) {
    tdf$end_session(driver)
  }
  
  invisible(NULL)
}

perform_task <- function(task, driver) {
  cli::cli_alert_info("Task: {.val {task}}.")
  
  rlang::try_fetch({
    switch(
      task,
      addition_subtraction = tdf$addition_subtraction(driver),
      multiplication = tdf$multiplication(driver)
    )
    cli::cli_alert_success("Task completed.")
  }, error = function(c) {
    cli::cli_alert_danger("Task failed.")
  })
}

dr_frost_tasks <- function() {
  c(
    "addition_subtraction", "multiplication"
  )
}
