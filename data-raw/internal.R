library(magrittr)

tasks_df <- tibble::tribble(
  ~topic, ~subtopic, ~task_name, ~description,
  "Algebra", "Sequences", "continue_sequence", "Continue a sequence.",
  "Algebra", "Sequences", "later_terms", "Find terms of a sequence given a term-to-term rule.",
  "Algebra", "Solving Equations", "simple_substitution", "Substitute into simple expressions (limited to addition, subtraction, division, multiplication).",
  "Algebra", "Solving Equations", "solve_one_step", "Solve linear equations where the variable appears on one side of the equation only.",
  "Data Handling & Probability", "Averages and Range", "mean", "Calculate the mean as an average.",
  "Data Handling & Probability", "Data Representation", "pictograms", "Interpret a pictogram.",
  "Data Handling & Probability", "Data Representation", "bar_charts", "Bar Charts",
  "Data Handling & Probability", "Data Representation", "bank_statements", "Complete a bank statement.",
  "Data Handling & Probability", "Data Representation", "pie_charts", "Pie Charts",
  "Number", "Arithmetic Operations", "addition_subtraction", "Add and subtract whole numbers.",
  "Number", "Arithmetic Operations", "multiplication", "Multiply numbers up to 3 digit by 3 digit.",
  "Number", "Arithmetic Operations", "pictoral_division", "Solve one step multiplication and division problems by using pictorial representations and arrays.",
  "Number", "Arithmetic Operations", "division", "Divide numbers.",
  "Number", "Arithmetic Operations", "number_facts", " Using number facts to solve connected calculations.",
  "Number", "Arithmetic Operations", "missing_digits", "Solve multiplication, addition and subtraction problems involving missing digits.",
  "Number", "Arithmetic Operations", "bidmas", "Understand the order in which operators in an expression are evaluated according to BIDMAS.",
  "Number", "Arithmetic Operations", "estimate_calculations", "Estimate the result of a calculation by first rounding each number.",
  "Number", "Decimals", "place_value", "Place value and ordering of decimals.",
  "Number", "Decimals", "decimal_addition_subtraction", "Add or subtract decimal numbers.",
  "Number", "Fraction, Decimal & Percentage Correspondences", "conversion", "Convert between non-recurring decimals, fractions and percentages.",
  "Number", "Fractions", "shape_fractions", "Find what fraction of a shape is shaded.",
  "Number", "Fractions", "equivalent_fractions", "Understand equivalent fractions.",
  "Number", "Fractions", "fraction_integer_division", "Divide fractions by integers.",
  "Number", "Fractions", "order_fractions", "Order fractions, possibly with decimals.",
  "Number", "Fractions", "mixed_addition_subtraction", "Add or subtract proper/improper fractions.",
  "Number", "Fractions", "fraction_amount", "Find a fraction of an amount.",
  "Number", "Fractions", "amount_before_fraction", "Find an original amount before a fraction of it was taken.",
  "Number", "Introduction to Negative Numbers", "order_negative_numbers", "Understand negative numbers on a number line, and order a mixture of negative and positive numbers.",
  
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

