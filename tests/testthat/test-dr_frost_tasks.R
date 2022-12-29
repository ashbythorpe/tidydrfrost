test_that("dr_frost_tasks() works", {
  expect_equal(dr_frost_tasks(), tasks_df[names(tasks_df) != "string"])
  
  expect_s3_class(dr_frost_tasks(), "dr_frost_tasks")
  expect_s3_class(dr_frost_tasks(), "tbl_df")
  
  expect_equal(nrow(dr_frost_tasks(include = "addition_subtraction")), 1)
  expect_equal(
    nrow(dr_frost_tasks(exclude = "addition_subtraction")), 
    nrow(dr_frost_tasks()) - 1
  )
  expect_length(unique(dr_frost_tasks(include = "KS2 Number")$topic), 1)
})

cli::test_that_cli("print method works", {
  expect_snapshot(expect_invisible(print(dr_frost_tasks())))
  expect_snapshot(expect_equal(print(dr_frost_tasks()), dr_frost_tasks()))
})
