get_account <- function(email, password, keyring) {
  if(is.null(password)) {
    accounts <- keyring::key_list("Dr Frost Maths", keyring = keyring)
    if(nrow(accounts) == 0) {
      cli::cli_abort(c(
        "No Dr Frost Accounts registered.",
        "i" = "Create an account with {.fun dr_frost_account}."
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
    cli::cli_alert_info("Getting account password for {.email {email}}.")
    
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
  
  # cli::cli_alert_info("Creating web session.")
  # 
  # driver <- rlang::try_fetch(
  #   tdf$driver_utils$create_driver(),
  #   error = function(c) {
  #     cli::cli_abort("Could not create web session.", parent = c)
  #   }
  # )
  
  cli::cli_alert_info("Logging in to Dr Frost Maths.")
  
  logged_in <- rlang::try_fetch(
    tdf$driver_utils$login(account$email, account$password),
    error = function(c) {
      tdf$driver_utils$end_session()
      cli::cli_abort("Could not log in.", parent = c)
    }
  )
  
  if(!logged_in) {
    tdf$driver_utils$end_session()
    cli::cli_abort("The username or password is incorrect.")
  }
  
  cli::cli_alert_success("Logged in successfully.")
}
