dr_frost_tasks <- function(include = NULL, exclude = NULL) {
  if(!is.null(include)) {
    vctrs::vec_assert(include, character())
  }
  if(!is.null(exclude)) {
    vctrs::vec_assert(exclude, character())
  }
  
  condition <- FALSE
  if(!is.null(include) && length(include) > 0) {
    for(a in include) {
      condition <- condition | create_filter(a)
    }
  } else {
    condition <- TRUE
  }
  
  if(!is.null(exclude) && length(exclude) > 0) {
    for(a in exclude) {
      condition <- condition & !create_filter(a)
    }
  }
  
  tasks_df[condition, names(tasks_df) != "string"]
}

create_filter <- function(x) {
  if(x %in% tasks_df$topic) {
    tasks_df$topic == x
  } else if(x %in% tasks_df$subtopic) {
    tasks_df$subtopic == x
  } else if(x %in% tasks_df$task_name) {
    tasks_df$task_name == x
  } else {
    grepl(x, tasks_df$string)
  }
}

#' @export
print.dr_frost_tasks <- function(x, ...) {
  cat(nrow(x), "Dr Frost tasks\n")
  cli::cli({
    d <- cli::cli_div(theme = list(
      h1 = list("margin-bottom" = 1),
      h2 = list("margin-bottom" = 0)
    ))
    for(a in unique(x$topic)) {
      cli::cli_h1(a)
      y <- x[x$topic == a,]
      for(b in unique(y$subtopic)) {
        cli::cli_div(
          cli::cli_h2(b),
          theme = list(h2 = list("margin-bottom" = 0))
        )
        z <- y[y$subtopic == b,]
        for(i in seq_len(nrow(z))) {
          row <- z[i,]
          cli::cli_bullets(c(
            "*" = row$task_name,
            " " = row$description
          ))
        }
      }
    }
    cli::cli_end(d)
  })
  invisible(x)
}

get_tasks <- function(tasks) {
  if(is.data.frame(tasks)) {
    tasks <- tasks[tasks$task_name %in% tasks_df$task_name,]
    if (nrow(tasks) == 0) {
      return()
    } else {
      tasks$task_name
    }
  } else {
    get_tasks(dr_frost_tasks(tasks))
  }
}
