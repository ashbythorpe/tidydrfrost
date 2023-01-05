#' Store your account details securely
#' 
#' Securely store the email and password to your Dr Frost Maths account so that
#' it can be used between sessions. The [keyring][keyring::keyring] 
#' package is used as a backend, meaning that credentials are stored securely 
#' and permanently.
#' 
#' @param email The email for your Dr Frost Account. Multiple accounts with
#'   different emails can be stored.
#' @param keyring A string, passed into [keyring::key_set()] and 
#'   [keyring::key_get()]. Use this to store your Dr Frost credentials on a
#'   custom keyring.
#' 
#' @details 
#' Calling this function should open a prompt, allowing you to enter your
#' password securely.
#' 
#' To change the password stored for a specific email, just call the function
#' again with the same email.
#' 
#' If the account you store is the first to be stored on the specified keyring, 
#' the account will be marked as a 'default' for the keyring. This means that
#' when [perform_tasks()] is called without specifying an email, this account
#' will be used as a default. Change this with [set_default_account()].
#' 
#' This means that once you have stored an account, the [perform_tasks()]
#' function can be called without specifying an email or password.
#' 
#' @returns Nothing. This function is called for its side effects.
#' 
#' @examples 
#' \dontrun{
#'   dr_frost_account("YOUR-EMAIL")
#'   perform_tasks()
#' }
#' 
#' @export
dr_frost_account <- function(email, keyring = NULL) {
  vctrs::vec_assert(email, ptype = character(), size = 1)
  
  usernames <- 
    keyring::key_list(service = "Dr Frost Maths", keyring = keyring)$username
  
  if(email %in% usernames) {
    cli::cli_alert_info("Changing password for {.email {email}}.")
  } else {
    cli::cli_alert_info("Setting password for {.email {email}}.")
  }
  
  rlang::try_fetch(
    keyring::key_set("Dr Frost Maths", username = email, keyring = keyring),
    error = function(c) {
      if(any(grepl(
        "Cannot create an item in a locked collection",
        as.character(c)
      ))) {
        # This can sometimes be solved by unlocking the keyring first
        set_key_manually(email, keyring)
      } else {
        cli::cli_abort("Setting password failed.", parent = c)
      }
    }
  )
  
  cli::cli_alert_success("Password set.")
  
  default <- tryCatch(
    keyring::key_get("tidydrfrost Default email", keyring = keyring),
    error = function(c) NULL
  )
  
  if(is.null(default)) {
    set_default_account(email, keyring)
  }
  
  invisible(NULL)
}

#' Set the default Dr Frost Maths account
#' 
#' Set or change the default email used by the [perform_tasks()] function.
#' 
#' @param email The email to use.
#' @param keyring A string, passed into [keyring::key_set()] and 
#'   [keyring::key_get()]. Use this if your Dr Frost accounts are
#'   stored on a custom keyring.
#' 
#' @returns Nothing. This function is called for its side effects.
#' 
#' @examples 
#' \dontrun{
#'   set_default_account("YOUR-EMAIL")
#' }
#' 
#' @export
set_default_account <- function(email, keyring = NULL) {
  cli::cli_alert_info("Setting {.email {email}} as default account.")
  
  rlang::try_fetch(
    keyring::key_set_with_value("tidydrfrost Default email", password = email,
                                keyring = keyring),
    error = function(c) {
      cli::cli_abort("Setting default account failed.", parent = c)
    }
  )
  
  cli::cli_alert_success("Default account set.")
  
  invisible(NULL)
}

set_key_manually <- function(email, keyring) {
  cli::cli_alert_danger("Setting password failed.")
  
  cli::cli_alert_info("Trying to unlock keyring manually.")
  
  rlang::try_fetch(
    keyring::keyring_unlock(keyring = keyring),
    error = function(c) {
      cli::cli_abort("Keyring could not be unlocked.", parent = c)
    }
  )
  
  rlang::try_fetch(
    keyring::key_set("Dr Frost Maths", username = email, keyring = keyring),
    error = function(c) {
      cli::cli_abort("Setting password failed.", parent = c)
    }
  )
}
