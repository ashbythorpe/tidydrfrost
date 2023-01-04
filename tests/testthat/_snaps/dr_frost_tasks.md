# print method works [plain]

    Code
      expect_invisible(print(dr_frost_tasks()))
    Message <cliMessage>
      # 10 Dr Frost tasks
      
      -- Algebra ---------------------------------------------------------------------
      
      -- Sequences --
      * continue_sequence
        Continue a sequence.
      * later_terms
        Find terms of a sequence given a term-to-term rule.
      
      -- Solving Equations --
      * simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      * solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      -- Data Handling & Probability -------------------------------------------------
      
      -- Averages and Range --
      * mean
        Calculate the mean as an average.
      
      -- Data Representation --
      * pictograms
        Interpret a pictogram.
      * bar_charts
        Bar Charts
      * bank_statements
        Complete a bank statement.
      * pie_charts
        Pie Charts
      
      -- Number ----------------------------------------------------------------------
      
      -- Arithmetic Operations --
      * addition_subtraction
        Add and subtract whole numbers.
      … with 16 more tasks
      # ℹ Use `print(n = ...)` to see more tasks

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      # 10 Dr Frost tasks
      
      -- Algebra ---------------------------------------------------------------------
      
      -- Sequences --
      * continue_sequence
        Continue a sequence.
      * later_terms
        Find terms of a sequence given a term-to-term rule.
      
      -- Solving Equations --
      * simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      * solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      -- Data Handling & Probability -------------------------------------------------
      
      -- Averages and Range --
      * mean
        Calculate the mean as an average.
      
      -- Data Representation --
      * pictograms
        Interpret a pictogram.
      * bar_charts
        Bar Charts
      * bank_statements
        Complete a bank statement.
      * pie_charts
        Pie Charts
      
      -- Number ----------------------------------------------------------------------
      
      -- Arithmetic Operations --
      * addition_subtraction
        Add and subtract whole numbers.
      … with 16 more tasks
      # ℹ Use `print(n = ...)` to see more tasks

# print method works [ansi]

    Code
      expect_invisible(print(dr_frost_tasks()))
    Message <cliMessage>
      [90m# 10 Dr Frost tasks[39m
      
      [36m--[39m [1mAlgebra[22m [36m---------------------------------------------------------------------[39m
      
      -- [1m[1mSequences[1m[22m --
      [36m*[39m continue_sequence
        Continue a sequence.
      [36m*[39m later_terms
        Find terms of a sequence given a term-to-term rule.
      
      -- [1m[1mSolving Equations[1m[22m --
      [36m*[39m simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      [36m*[39m solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      [36m--[39m [1mData Handling & Probability[22m [36m-------------------------------------------------[39m
      
      -- [1m[1mAverages and Range[1m[22m --
      [36m*[39m mean
        Calculate the mean as an average.
      
      -- [1m[1mData Representation[1m[22m --
      [36m*[39m pictograms
        Interpret a pictogram.
      [36m*[39m bar_charts
        Bar Charts
      [36m*[39m bank_statements
        Complete a bank statement.
      [36m*[39m pie_charts
        Pie Charts
      
      [36m--[39m [1mNumber[22m [36m----------------------------------------------------------------------[39m
      
      -- [1m[1mArithmetic Operations[1m[22m --
      [36m*[39m addition_subtraction
        Add and subtract whole numbers.
      [90m… with 16 more tasks[39m
      [90m# ℹ Use `print(n = ...)` to see more tasks[39m

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      [90m# 10 Dr Frost tasks[39m
      
      [36m--[39m [1mAlgebra[22m [36m---------------------------------------------------------------------[39m
      
      -- [1m[1mSequences[1m[22m --
      [36m*[39m continue_sequence
        Continue a sequence.
      [36m*[39m later_terms
        Find terms of a sequence given a term-to-term rule.
      
      -- [1m[1mSolving Equations[1m[22m --
      [36m*[39m simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      [36m*[39m solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      [36m--[39m [1mData Handling & Probability[22m [36m-------------------------------------------------[39m
      
      -- [1m[1mAverages and Range[1m[22m --
      [36m*[39m mean
        Calculate the mean as an average.
      
      -- [1m[1mData Representation[1m[22m --
      [36m*[39m pictograms
        Interpret a pictogram.
      [36m*[39m bar_charts
        Bar Charts
      [36m*[39m bank_statements
        Complete a bank statement.
      [36m*[39m pie_charts
        Pie Charts
      
      [36m--[39m [1mNumber[22m [36m----------------------------------------------------------------------[39m
      
      -- [1m[1mArithmetic Operations[1m[22m --
      [36m*[39m addition_subtraction
        Add and subtract whole numbers.
      [90m… with 16 more tasks[39m
      [90m# ℹ Use `print(n = ...)` to see more tasks[39m

# print method works [unicode]

    Code
      expect_invisible(print(dr_frost_tasks()))
    Message <cliMessage>
      # 10 Dr Frost tasks
      
      ── Algebra ─────────────────────────────────────────────────────────────────────
      
      ── Sequences ──
      • continue_sequence
        Continue a sequence.
      • later_terms
        Find terms of a sequence given a term-to-term rule.
      
      ── Solving Equations ──
      • simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      • solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      ── Data Handling & Probability ─────────────────────────────────────────────────
      
      ── Averages and Range ──
      • mean
        Calculate the mean as an average.
      
      ── Data Representation ──
      • pictograms
        Interpret a pictogram.
      • bar_charts
        Bar Charts
      • bank_statements
        Complete a bank statement.
      • pie_charts
        Pie Charts
      
      ── Number ──────────────────────────────────────────────────────────────────────
      
      ── Arithmetic Operations ──
      • addition_subtraction
        Add and subtract whole numbers.
      … with 16 more tasks
      # ℹ Use `print(n = ...)` to see more tasks

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      # 10 Dr Frost tasks
      
      ── Algebra ─────────────────────────────────────────────────────────────────────
      
      ── Sequences ──
      • continue_sequence
        Continue a sequence.
      • later_terms
        Find terms of a sequence given a term-to-term rule.
      
      ── Solving Equations ──
      • simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      • solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      ── Data Handling & Probability ─────────────────────────────────────────────────
      
      ── Averages and Range ──
      • mean
        Calculate the mean as an average.
      
      ── Data Representation ──
      • pictograms
        Interpret a pictogram.
      • bar_charts
        Bar Charts
      • bank_statements
        Complete a bank statement.
      • pie_charts
        Pie Charts
      
      ── Number ──────────────────────────────────────────────────────────────────────
      
      ── Arithmetic Operations ──
      • addition_subtraction
        Add and subtract whole numbers.
      … with 16 more tasks
      # ℹ Use `print(n = ...)` to see more tasks

# print method works [fancy]

    Code
      expect_invisible(print(dr_frost_tasks()))
    Message <cliMessage>
      [90m# 10 Dr Frost tasks[39m
      
      [36m──[39m [1mAlgebra[22m [36m─────────────────────────────────────────────────────────────────────[39m
      
      ── [1m[1mSequences[1m[22m ──
      [36m•[39m continue_sequence
        Continue a sequence.
      [36m•[39m later_terms
        Find terms of a sequence given a term-to-term rule.
      
      ── [1m[1mSolving Equations[1m[22m ──
      [36m•[39m simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      [36m•[39m solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      [36m──[39m [1mData Handling & Probability[22m [36m─────────────────────────────────────────────────[39m
      
      ── [1m[1mAverages and Range[1m[22m ──
      [36m•[39m mean
        Calculate the mean as an average.
      
      ── [1m[1mData Representation[1m[22m ──
      [36m•[39m pictograms
        Interpret a pictogram.
      [36m•[39m bar_charts
        Bar Charts
      [36m•[39m bank_statements
        Complete a bank statement.
      [36m•[39m pie_charts
        Pie Charts
      
      [36m──[39m [1mNumber[22m [36m──────────────────────────────────────────────────────────────────────[39m
      
      ── [1m[1mArithmetic Operations[1m[22m ──
      [36m•[39m addition_subtraction
        Add and subtract whole numbers.
      [90m… with 16 more tasks[39m
      [90m# ℹ Use `print(n = ...)` to see more tasks[39m

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      [90m# 10 Dr Frost tasks[39m
      
      [36m──[39m [1mAlgebra[22m [36m─────────────────────────────────────────────────────────────────────[39m
      
      ── [1m[1mSequences[1m[22m ──
      [36m•[39m continue_sequence
        Continue a sequence.
      [36m•[39m later_terms
        Find terms of a sequence given a term-to-term rule.
      
      ── [1m[1mSolving Equations[1m[22m ──
      [36m•[39m simple_substitution
        Substitute into simple expressions (limited to addition, subtraction,
        division, multiplication).
      [36m•[39m solve_one_step
        Solve linear equations where the variable appears on one side of the equation
        only.
      
      [36m──[39m [1mData Handling & Probability[22m [36m─────────────────────────────────────────────────[39m
      
      ── [1m[1mAverages and Range[1m[22m ──
      [36m•[39m mean
        Calculate the mean as an average.
      
      ── [1m[1mData Representation[1m[22m ──
      [36m•[39m pictograms
        Interpret a pictogram.
      [36m•[39m bar_charts
        Bar Charts
      [36m•[39m bank_statements
        Complete a bank statement.
      [36m•[39m pie_charts
        Pie Charts
      
      [36m──[39m [1mNumber[22m [36m──────────────────────────────────────────────────────────────────────[39m
      
      ── [1m[1mArithmetic Operations[1m[22m ──
      [36m•[39m addition_subtraction
        Add and subtract whole numbers.
      [90m… with 16 more tasks[39m
      [90m# ℹ Use `print(n = ...)` to see more tasks[39m

