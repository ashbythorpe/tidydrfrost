fixed_time <- function() {
  points <- NA
  error <- NA
  
  error <- rlang::try_fetch({
    tdf$times_tables$fixed_time()
    cli::cli_alert_success("Task completed.")
  }, error = function(c) {
    cli::cli_alert_danger("Task failed.")
    c
  })
  
  if(all(is.na(error))) {
    error <- rlang::try_fetch({
      points <- tdf$times_tables$times_tables_points()
      cli::cli_alert_success("Points obtained: {.val {points}}.")
      NA
    }, error = function(c) {
      cli::cli_alert_danger("Could not get points.")
      c
    })
  }
  
  list(
    completed = !is.na(points),
    points = points,
    error = error
  )
}

individual_practice <- function() {
  total_points <- NA
  error_list <- list()
  completed <- 0
  
  for(i in 1:29) {
    points <- NA
    error <- NA
    
    error <- rlang::try_fetch({
      tdf$times_tables$individual_practice(i)
    }, error = function(c) {
      c
    })
    
    if(all(is.na(error))) {
      error <- rlang::try_fetch({
        points <- tdf$times_tables$times_tables_points()
        completed <- completed + 1
      }, error = function(c) {
        cli::cli_alert_danger("Could not get points.")
        c
      })
    }
    
    if(!all(is.na(error))) {
      error_list <- c(error_list, list(error))
    } else {
      total_points <- add_points(total_points, points)
    }
  }
  
  if(completed == 0) {
    cli::cli_alert_danger("Task failed.")
  } else {
    cli::cli_alert_success("Completed {completed}/29 times table games.")
    cli::cli_alert_success("Points obtained: {.val {total_points}}.")
  }
  
  list(
    completed = completed != 0,
    points = total_points,
    error = error_list
  )
}

add_points <- function(existing, new) {
  if(is.na(existing)) {
    new
  } else {
    existing + new
  }
}
