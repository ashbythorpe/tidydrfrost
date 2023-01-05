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
      ... with 16 more tasks
      # i Use `print(n = ...)` to see more tasks

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
      ... with 16 more tasks
      # i Use `print(n = ...)` to see more tasks

---

    Code
      print(dr_frost_tasks(), n = Inf)
    Message <cliMessage>
      # 26 Dr Frost tasks
      
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
      * multiplication
        Multiply numbers up to 3 digit by 3 digit.
      * pictoral_division
        Solve one step multiplication and division problems by using pictorial
        representations and arrays.
      * division
        Divide numbers.
      * number_facts
        Using number facts to solve connected calculations.
      * missing_digits
        Solve multiplication, addition and subtraction problems involving missing
        digits.
      * bidmas
        Understand the order in which operators in an expression are evaluated
        according to BIDMAS.
      * estimate_calculations
        Estimate the result of a calculation by first rounding each number.
      
      -- Decimals --
      * place_value
        Place value and ordering of decimals.
      * decimal_addition_subtraction
        Add or subtract decimal numbers.
      
      -- Fraction, Decimal & Percentage Correspondences --
      * conversion
        Convert between non-recurring decimals, fractions and percentages.
      
      -- Fractions --
      * shape_fractions
        Find what fraction of a shape is shaded.
      * equivalent_fractions
        Understand equivalent fractions.
      * fraction_integer_division
        Divide fractions by integers.
      * order_fractions
        Order fractions, possibly with decimals.
      
      -- Times tables ----------------------------------------------------------------
      
      * fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      * individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

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
      [90m... with 16 more tasks[39m
      [90m# i Use `print(n = ...)` to see more tasks[39m

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
      [90m... with 16 more tasks[39m
      [90m# i Use `print(n = ...)` to see more tasks[39m

---

    Code
      print(dr_frost_tasks(), n = Inf)
    Message <cliMessage>
      [90m# 26 Dr Frost tasks[39m
      
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
      [36m*[39m multiplication
        Multiply numbers up to 3 digit by 3 digit.
      [36m*[39m pictoral_division
        Solve one step multiplication and division problems by using pictorial
        representations and arrays.
      [36m*[39m division
        Divide numbers.
      [36m*[39m number_facts
        Using number facts to solve connected calculations.
      [36m*[39m missing_digits
        Solve multiplication, addition and subtraction problems involving missing
        digits.
      [36m*[39m bidmas
        Understand the order in which operators in an expression are evaluated
        according to BIDMAS.
      [36m*[39m estimate_calculations
        Estimate the result of a calculation by first rounding each number.
      
      -- [1m[1mDecimals[1m[22m --
      [36m*[39m place_value
        Place value and ordering of decimals.
      [36m*[39m decimal_addition_subtraction
        Add or subtract decimal numbers.
      
      -- [1m[1mFraction, Decimal & Percentage Correspondences[1m[22m --
      [36m*[39m conversion
        Convert between non-recurring decimals, fractions and percentages.
      
      -- [1m[1mFractions[1m[22m --
      [36m*[39m shape_fractions
        Find what fraction of a shape is shaded.
      [36m*[39m equivalent_fractions
        Understand equivalent fractions.
      [36m*[39m fraction_integer_division
        Divide fractions by integers.
      [36m*[39m order_fractions
        Order fractions, possibly with decimals.
      
      [36m--[39m [1mTimes tables[22m [36m----------------------------------------------------------------[39m
      
      [36m*[39m fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      [36m*[39m individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

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

---

    Code
      print(dr_frost_tasks(), n = Inf)
    Message <cliMessage>
      # 26 Dr Frost tasks
      
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
      • multiplication
        Multiply numbers up to 3 digit by 3 digit.
      • pictoral_division
        Solve one step multiplication and division problems by using pictorial
        representations and arrays.
      • division
        Divide numbers.
      • number_facts
        Using number facts to solve connected calculations.
      • missing_digits
        Solve multiplication, addition and subtraction problems involving missing
        digits.
      • bidmas
        Understand the order in which operators in an expression are evaluated
        according to BIDMAS.
      • estimate_calculations
        Estimate the result of a calculation by first rounding each number.
      
      ── Decimals ──
      • place_value
        Place value and ordering of decimals.
      • decimal_addition_subtraction
        Add or subtract decimal numbers.
      
      ── Fraction, Decimal & Percentage Correspondences ──
      • conversion
        Convert between non-recurring decimals, fractions and percentages.
      
      ── Fractions ──
      • shape_fractions
        Find what fraction of a shape is shaded.
      • equivalent_fractions
        Understand equivalent fractions.
      • fraction_integer_division
        Divide fractions by integers.
      • order_fractions
        Order fractions, possibly with decimals.
      
      ── Times tables ────────────────────────────────────────────────────────────────
      
      • fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      • individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

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

---

    Code
      print(dr_frost_tasks(), n = Inf)
    Message <cliMessage>
      [90m# 26 Dr Frost tasks[39m
      
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
      [36m•[39m multiplication
        Multiply numbers up to 3 digit by 3 digit.
      [36m•[39m pictoral_division
        Solve one step multiplication and division problems by using pictorial
        representations and arrays.
      [36m•[39m division
        Divide numbers.
      [36m•[39m number_facts
        Using number facts to solve connected calculations.
      [36m•[39m missing_digits
        Solve multiplication, addition and subtraction problems involving missing
        digits.
      [36m•[39m bidmas
        Understand the order in which operators in an expression are evaluated
        according to BIDMAS.
      [36m•[39m estimate_calculations
        Estimate the result of a calculation by first rounding each number.
      
      ── [1m[1mDecimals[1m[22m ──
      [36m•[39m place_value
        Place value and ordering of decimals.
      [36m•[39m decimal_addition_subtraction
        Add or subtract decimal numbers.
      
      ── [1m[1mFraction, Decimal & Percentage Correspondences[1m[22m ──
      [36m•[39m conversion
        Convert between non-recurring decimals, fractions and percentages.
      
      ── [1m[1mFractions[1m[22m ──
      [36m•[39m shape_fractions
        Find what fraction of a shape is shaded.
      [36m•[39m equivalent_fractions
        Understand equivalent fractions.
      [36m•[39m fraction_integer_division
        Divide fractions by integers.
      [36m•[39m order_fractions
        Order fractions, possibly with decimals.
      
      [36m──[39m [1mTimes tables[22m [36m────────────────────────────────────────────────────────────────[39m
      
      [36m•[39m fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      [36m•[39m individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

