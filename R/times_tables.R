times_tables <- function(iter = 1, email = NULL, keyring = NULL, end = TRUE) {
  vctrs::vec_assert(iter, size = 1)
  iter <- vctrs::vec_cast(iter, integer())
  if(iter < 1) {
    cli::cli_abort("{.arg iter} must be positive.")
  }
  
  account <- get_account(email, keyring)
  
  driver <- tdf$create_driver()
  
  tdf$login(driver, account$email, account$password)
  
  for(i in seq_len(iter)) {
    tdf$times_tables_iter(driver)
  }
  
  if(end) tdf$end_session(driver)
}

times_tables_games <- function(n = 1:29, email = NULL, keyring = NULL) {
  n <- vctrs::vec_cast(n, integer())
  
  account <- get_account(email, keyring)
  
  driver <- tdf$create_driver()
  
  tdf$login(driver, account$email, account$password)
  
  for(i in n) {
    tdf$times_tables_game(driver, i)
  }
  
  if(end) tdf$end_session(driver)
}

get_account <- function(email, keyring) {
  accounts <- keyring::key_list("Dr Frost Maths", keyring = keyring)
  if(nrow(accounts) == 0) {
    cli::cli_abort(c(
      "No Dr Frost Accounts registered.",
      "i" = "Create an account with {.fun dr_frost_account}"
    ))
  }
  
  if(is.null(email)) {
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
  
  password <- keyring::key_get(
    "Dr Frost Maths", 
    username = email, 
    keyring = keyring
  )
  
  list(
    email = email,
    password = password
  )
}
