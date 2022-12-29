library(magrittr)

tasks_df <- tibble::tribble(
  ~topic, ~subtopic, ~task_name, ~description,
  "KS2 Number", "Arithmetic Operations", "addition_subtraction", "Add and subtract whole numbers.",
  "KS2 Number", "Arithmetic Operations", "multiplication", "Multiply numbers up to 3 digit by 3 digit.",
  "KS2 Number", "Arithmetic Operations", "pictoral_division", "Solve one step multiplication and division problems by using pictorial representations and arrays.",
  "KS2 Number", "Arithmetic Operations", "division", "Divide numbers.",
  "KS2 Number", "Arithmetic Operations", "number_facts", " Using number facts to solve connected calculations.",
  "KS2 Number", "Arithmetic Operations", "missing_digits", "Solve multiplication, addition and subtraction problems involving missing digits.",
  "KS2 Number", "Arithmetic Operations", "bidmas", "Understand the order in which operators in an expression are evaluated according to BIDMAS.",
  "KS2 Number", "Arithmetic Operations", "estimate_calculations", "Estimate the result of a calculation by first rounding each number.",
  
  "Times tables", "", "fixed_time", "You have 30 seconds to answer as many questions as you can on all times/divide tables. Can you get on the leaderboard?",
  "Times tables", "", "individual_practice", "Practise each times table/divide table separately, with points for accuracy and speed."
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

