tasks_df <- tibble::tribble(
  ~topic, ~subtopic, ~task_name, ~description,
  "KS3 Number", "Arithmetic Operations", "addition_subtraction", "Add and subtract whole numbers.",
  "KS3 Number", "Arithmetic Operations", "multiplication", "Multiply numbers up to 3 digit by 3 digit.",
  "KS3 Number", "Arithmetic Operations", "pictoral_division", "Solve one step multiplication and division problems by using pictorial representations and arrays."
) %>%
  dplyr::mutate(string = paste(topic, subtopic, task_name, description))

class(tasks_df) <- c("dr_frost_tasks", class(tasks_df))

result_init <- tibble::tibble(
  task = character(),
  completed = logical(),
  points = integer(),
  error = list(),
  .rows = 0
)

usethis::use_data(tasks_df, result_init, internal = TRUE, overwrite = TRUE)
