times_tables <- function(iter = 1, email = NULL, password = NULL, 
                         keyring = NULL, end = TRUE) {
  vctrs::vec_assert(iter, size = 1)
  iter <- vctrs::vec_cast(iter, integer())
  if(iter < 1) {
    cli::cli_abort("{.arg iter} must be positive.")
  }
  
  driver <- driver_setup(email, keyring, password)
  
  cli::cli_alert_info("Running times table task.")
  
  for(i in seq_len(iter)) {
    tdf$times_tables_iter(driver)
  }
  
  cli::cli_alert_success("Times tables task finished.")
  
  if(end) {
    tdf$end_session(driver)
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
  
  driver <- driver_setup(email, keyring, password)
  
  cli::cli_alert_info("Running times table games.")
  
  for(i in n) {
    tdf$times_tables_game(driver, i)
  }
  
  cli::cli_alert_success("Times tables games finished.")
  
  if(end) {
    tdf$end_session(driver)
  }
  
  invisible(NULL)
}

get_account <- function(email, password, keyring) {
  if(is.null(password)) {
    accounts <- keyring::key_list("Dr Frost Maths", keyring = keyring)
    if(nrow(accounts) == 0) {
      cli::cli_abort(c(
        "No Dr Frost Accounts registered.",
        "i" = "Create an account with {.fun dr_frost_account}"
      ))
    }
  }
  
  if(is.null(email)) {
    cli::cli_alert_info("Finding default account.")
    email <- tryCatch(
      keyring::key_get("tidydrfrost Default email", keyring = keyring),
      error = function(c) {
        cli::cli_abort(c(
          "Default account not found.",
          "i" = "Try specifying {.arg email} manually."
        ))
      }
    )
  }
  
  if(is.null(password)) {
    cli::cli_alert_info("Getting account password for {.email {email}}")
    
    password <- rlang::try_fetch(
      keyring::key_get(
        "Dr Frost Maths", 
        username = email, 
        keyring = keyring
      ),
      error = function(c) {
        cli::cli_abort("Password could not be retrieved.", parent = c)
      }
    )
    
    cli::cli_alert_success("Password retrieved successfully.")
  }
  
  list(
    email = email,
    password = password
  )
}

driver_setup <- function(email, password, keyring) {
  account <- get_account(email, password, keyring)
  
  cli::cli_alert_info("Creating web session.")
  
  driver <- rlang::try_fetch(
    tdf$create_driver(),
    error = function(c) {
      cli::cli_abort("Could not create web session.", parent = c)
    }
  )
  
  cli::cli_alert_info("Logging in to Dr Frost Maths.")
  
  rlang::try_fetch(
    tdf$login(driver, account$email, account$password),
    error = function(c) {
      cli::cli_abort("Could not log in.", parent = c)
    }
  )
  
  cli::cli_alert_success("Logged in successfully.")
  
  driver
}
