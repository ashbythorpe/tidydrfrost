#' Get the set of available tasks
#' 
#' Retrieve a set of tasks that can be completed in 
#' [Dr Frost Maths](https://www.drfrostmaths.com/), choosing tasks to include
#' and exclude.
#' 
#' @param include A character vector of tasks to include. If `NULL`, all tasks
#'   will be included.
#' @param exclude A character vector of tasks to exclude. If `NULL`, no tasks
#'   will be excluded.
#' @param x A `dr_frost_tasks` object.
#' @param ... Not used.
#'
#' @details 
#' If the `include` argument matches a topic, subtopic or task name of any task,
#' tasks will require a direct match with the string to be included. Otherwise,
#' partial matching/pattern recognition will be used to identify matches.
#' 
#' The same applies to the `exclude` argument.
#' 
#' While this makes specifying tasks simple most of the time, it can sometimes
#' lead to some unexpected cases where more complex searches result in less
#' matches.
#' 
#' @returns 
#' A data frame with additional class 'dr_frost_tasks', where each row
#' describes a task. The table has 4 variables:
#' \describe{
#'   \item{topic}{The topic that the task falls under.}
#'   \item{subtopic}{The subtopic of the task.}
#'   \item{task_name}{The name of the task.}
#'   \item{description}{A brief description of the task.}
#' }
#' 
#' @seealso [perform_tasks()]
#' 
#' @examples 
#' dr_frost_tasks()
#' 
#' dr_frost_tasks(include = "addition_subtraction")
#' 
#' dr_frost_tasks(include = "Arithmetic Operations")
#' 
#' dr_frost_tasks(include = "KS3 Number")
#' 
#' dr_frost_tasks(include = "KS3", exclude = "Arithmetic")
#' 
#' dr_frost_tasks(exclude = "addition")
#' 
#' tibble::as_tibble(dr_frost_tasks())
#' 
#' @export
dr_frost_tasks <- function(include = NULL, exclude = NULL) {
  if(!is.null(include) && length(include) == 0) {
    # Use drop = FALSE in case the user doesn't have tibble installed
    return(tasks_df[FALSE, , drop = FALSE])
  }
  if(!is.null(include)) {
    vctrs::vec_assert(include, character())
  }
  if(!is.null(exclude)) {
    vctrs::vec_assert(exclude, character())
  }
  
  condition <- FALSE
  if(!is.null(include)) {
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
  
  tasks_df[condition, names(tasks_df) != "string", drop = FALSE]
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

#' Printing Dr Frost tasks
#' 
#' The `dr_frost_tasks` object has an enhanced printing method, using topics and
#' subtopics as headers.
#' 
#' @param x A `dr_frost_tasks` object.
#' @param ... Not used.
#' @param n The maximum number of tasks to show. Excess tasks will be truncated.
#'   Use `Inf` to show all tasks.
#' 
#' @details 
#' This printing method is heavily inspired by the tibble printing method:
#' [tibble::print.tbl_df].
#' 
#' @returns `x`, invisibly
#' 
#' @examples 
#' print(dr_frost_tasks())
#' print(dr_frost_tasks(), n = 5)
#' 
#' @export
print.dr_frost_tasks <- function(x, ..., n = 10) {
  vctrs::vec_assert(n, size = 1)
  if(!is.infinite(n)) {
    n <- vctrs::vec_cast(n, integer())
  }
  grey <- cli::make_ansi_style("grey60", grey = TRUE)
  
  data <- x
  
  if(nrow(data) == 0L) {
    cli::cli_text(grey("# 0 Dr Frost tasks"))
    return(invisible(x))
  } else if(n == 0L || (n < 0L && -n >= nrow(x))) {
    cli::cli_text(grey("# {nrow(x)} Dr Frost task{?s}"))
    cli::cli_text(grey("… with {nrow(x)} more task{?s}"))
    cli::cli_text(grey("# ℹ Use `print(n = ...)` to see more tasks"))
    return(invisible(x))
  } else if(n < 0L) {
    excess_tasks <- -n
    data <- data[-seq_len(-n),]
  } else if(nrow(data) > n) {
    excess_tasks <- nrow(x) - n
    data <- data[seq_len(n),]
  } else {
    excess_tasks <- NA
  }
  
  print_dr_frost_tasks(data, excess_tasks, grey)
  
  invisible(x)
}

print_dr_frost_tasks <- function(x, excess_tasks, grey) {
  cli::cli({
    cli::cli_text(grey("# {nrow(x)} Dr Frost task{?s}"))
    d <- cli::cli_div(theme = list(
      h1 = list("margin-bottom" = 1),
      h2 = list("margin-bottom" = 0)
    ))
    for(a in unique(x$topic)) {
      if(a != "") {
        cli::cli_h1(a)
      }
      y <- x[x$topic == a, , drop = FALSE]
      for(b in unique(y$subtopic)) {
        if(b != "") {
          cli::cli_h2(b)
        }
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
    if(!is.na(excess_tasks)) {
      cli::cli_text(grey("… with {excess_tasks} more task{?s}"))
      cli::cli_text(grey("# ℹ Use `print(n = ...)` to see more tasks"))
    }
  })
}

get_tasks <- function(tasks) {
  if(is.data.frame(tasks)) {
    tasks <- tasks[tasks$task_name %in% tasks_df$task_name, , drop = FALSE]
    if (nrow(tasks) == 0) {
      return()
    } else {
      tasks$task_name
    }
  } else {
    get_tasks(dr_frost_tasks(tasks))
  }
}
