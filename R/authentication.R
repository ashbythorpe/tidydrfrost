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
  
  if(length(usernames) == 0) {
    cli::cli_alert_info("Setting {.email {email}} as default account.")
    keyring::key_set_with_value("tidydrfrost Default email", email)
    cli::cli_alert_success("Default account set.")
  }
}
