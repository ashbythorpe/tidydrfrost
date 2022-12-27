skip_if_no_selene <- function() {
  if (!reticulate::py_module_available("selene")) {
    skip("selene not available for testing")
  }
}

test_that("perform_tasks() works", {
  skip_if_no_selene()
  skip_if_offline()
  
  
})
