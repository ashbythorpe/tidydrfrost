
<!-- README.md is generated from README.Rmd. Please edit that file -->

# tidydrfrost

<!-- badges: start -->

[![Codecov test
coverage](https://codecov.io/gh/ashbythorpe/tidydrfrost/branch/master/graph/badge.svg)](https://app.codecov.io/gh/ashbythorpe/tidydrfrost?branch=master)
[![R-CMD-check](https://github.com/ashbythorpe/tidydrfrost/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/ashbythorpe/tidydrfrost/actions/workflows/R-CMD-check.yaml)
<!-- badges: end -->

tidydrfrost allows you to automate and complete [Dr Frost
Maths](https://www.drfrostmaths.com/) tasks using R. This allows points
and mastery to be quickly and easily gained.

## Installation

You can install the development version of tidydrfrost from
[GitHub](https://github.com/) with:

``` r
# install.packages("devtools")
devtools::install_github("ashbythorpe/tidydrfrost")
```

## Using the package

Interacting with [Dr Frost Maths](https://www.drfrostmaths.com/) is very
simple.

``` r
library(tidydrfrost)
```

The package revolves around a single function:

``` r
perform_tasks()
```

This function will perform all tasks that have been implemented. Each
task awards a certain number of points. Alternatively, you can specify
the tasks to complete:

``` r
perform_tasks(c("addition_subtraction", "multiplication"))
```

For a more controlled approach to specifying tasks, use the
`dr_frost_tasks()` function.

``` r
tasks <- dr_frost_tasks(exclude = "division")
perform_tasks(tasks)
```

Currently the following tasks have been implemented:

``` r
print(dr_frost_tasks(), n = Inf)
```

<picture>
<source media="(prefers-color-scheme: dark)" srcset="man/figures/README-/tasks-dark.svg">
<img src="man/figures/README-/tasks.svg" width="100%" /> </picture>

## Logging in

For the `perform_tasks()` function to work, you need to specify a Dr
Frost Maths account.

``` r
perform_tasks(
  email = "YOUR-EMAIL",
  password = "YOUR-PASSWORD"
)
```

If you don’t want to specify this each time you use the function, use
the `dr_frost_account()` function. This uses
[keyring](https://r-lib.github.io/keyring) as its backend, allowing your
credentials to be securely stored between sessions.

``` r
dr_frost_account("YOUR-EMAIL")
```

Once you have stored your account, the `perform_tasks()` function can be
called without having to specify an email or password.
