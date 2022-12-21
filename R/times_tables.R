times_tables <- function(iter = 1, email = NULL, password = NULL, 
                         keyring = NULL, end = TRUE) {
  vctrs::vec_assert(iter, size = 1)
  iter <- vctrs::vec_cast(iter, integer())
  if(iter < 1) {
    cli::cli_abort("{.arg iter} must be positive.")
  }
  
  driver <- driver_setup(email, password, keyring)
  
  cli::cli_alert_info("Running times table task.")
  
  for(i in seq_len(iter)) {
    tdf$times_tables$times_tables_iter(driver)
  }
  
  cli::cli_alert_success("Times tables task finished.")
  
  if(end) {
    tdf$driver_utils$end_session(driver)
  }
  
  invisible(NULL)
}

times_tables_games <- function(n = 1:29, email = NULL, password = NULL, 
                               keyring = NULL, end = TRUE) {
  n <- vctrs::vec_cast(n, integer())
  if(length(n) == 0) {
    cli::cli_abort("{.arg n} must not be an empty vector.")
  }
  n <- n[n >= 1L & n <= 29L]
  if(length(n) == 0) {
    cli::cli_abort("{.arg n} must be between 0 and 29.")
  }
  
  driver <- driver_setup(email, password, keyring)
  
  cli::cli_alert_info("Running times table games.")
  
  for(i in n) {
    tdf$times_tables$times_tables_game(driver, i)
  }
  
  cli::cli_alert_success("Times tables games finished.")
  
  if(end) {
    tdf$driver_utils$end_session(driver)
  }
  
  invisible(NULL)
}
