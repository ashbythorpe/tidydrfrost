# print method works [plain]

    Code
      expect_invisible(print(dr_frost_tasks()))
    Message <cliMessage>
      # 7 Dr Frost tasks
      
      -- KS3 Number ------------------------------------------------------------------
      
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
      
      -- Times tables ----------------------------------------------------------------
      
      * fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      * individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      # 7 Dr Frost tasks
      
      -- KS3 Number ------------------------------------------------------------------
      
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
      [90m# 7 Dr Frost tasks[39m
      
      [36m--[39m [1mKS3 Number[22m [36m------------------------------------------------------------------[39m
      
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
      
      [36m--[39m [1mTimes tables[22m [36m----------------------------------------------------------------[39m
      
      [36m*[39m fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      [36m*[39m individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      [90m# 7 Dr Frost tasks[39m
      
      [36m--[39m [1mKS3 Number[22m [36m------------------------------------------------------------------[39m
      
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
      # 7 Dr Frost tasks
      
      ── KS3 Number ──────────────────────────────────────────────────────────────────
      
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
      
      ── Times tables ────────────────────────────────────────────────────────────────
      
      • fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      • individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      # 7 Dr Frost tasks
      
      ── KS3 Number ──────────────────────────────────────────────────────────────────
      
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
      [90m# 7 Dr Frost tasks[39m
      
      [36m──[39m [1mKS3 Number[22m [36m──────────────────────────────────────────────────────────────────[39m
      
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
      
      [36m──[39m [1mTimes tables[22m [36m────────────────────────────────────────────────────────────────[39m
      
      [36m•[39m fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      [36m•[39m individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

---

    Code
      expect_equal(print(dr_frost_tasks()), dr_frost_tasks())
    Message <cliMessage>
      [90m# 7 Dr Frost tasks[39m
      
      [36m──[39m [1mKS3 Number[22m [36m──────────────────────────────────────────────────────────────────[39m
      
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
      
      [36m──[39m [1mTimes tables[22m [36m────────────────────────────────────────────────────────────────[39m
      
      [36m•[39m fixed_time
        You have 30 seconds to answer as many questions as you can on all
        times/divide tables. Can you get on the leaderboard?
      [36m•[39m individual_practice
        Practise each times table/divide table separately, with points for accuracy
        and speed.

