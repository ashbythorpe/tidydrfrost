dr_frost_account <- function(email = NULL, keyring = NULL) {
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
}

set_default_account <- function(email, keyring) {
  cli::cli_alert_info("Setting {.email {email}} as default account.")
  
  rlang::try_fetch(
    keyring::key_set_with_value("tidydrfrost Default email", password = email,
                                keyring = keyring),
    error = function(c) {
      cli::cli_abort("Setting default account failed.", parent = c)
    }
  )
  
  cli::cli_alert_success("Default account set.")
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
