dr_frost_account <- function(email = NULL, keyring = NULL) {
  vctrs::vec_assert(email, ptype = character(), size = 1)
  
  usernames <- 
    keyring::key_list(service = "Dr Frost Maths", keyring = keyring)$username
  
  if(email %in% usernames) {
    cli::cli_alert_info("Changing password for {.email {email}}.")
  } else {
    cli::cli_alert_info("Setting password for {.email {email}}.")
  }
  
  keyring::key_set("Dr Frost Maths", username = email, keyring = keyring)
  
  cli::cli_alert_success("Password set.")
  
  default <- tryCatch(
    keyring::key_get("tidydrfrost Default email", keyring = keyring),
    error = function(c) NULL
  )
  
  if(is.null(default)) {
    cli::cli_alert_info("Setting {.email {email}} as default account.")
    keyring::key_set_with_value("tidydrfrost Default email", password = email)
    cli::cli_alert_success("Default account set.")
  }
}
