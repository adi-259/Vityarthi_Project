## Quiz App

A Python quiz application with a bank of more than **100 questions**. I have made this application to get integrated in a quiz platform or website which can be used for exam prep and other general practice purposes, currently it doesn't have much question, but i'll add more questions and for diffrent subjects.

Let's see what it provides and how i made this and how to use it.

## Randomization
- More than 100 questions are stored in `questions.py`.
- Each quiz attempt randomly selects 10 unique questions using `random.sample()` module.
- The selected question order changes after each run.
- No question repeats within the same attempt.
- Change `Quiz(question_count=10)` to any value for no. of question per attempt in `quiz.py`.

## Run
```bash
python main.py
```

## Files
- `main.py` — starts the application
- `quiz.py` — quiz engine and random question selection
- `questions.py` — question bank
- `scoring.py` — score calculation
- `algorithms.py` — counting, maximum and selection-sort helpers
- `leaderboard.py` — result/leaderboard helpers
- `PROJECT_DOCUMENTATION.md` — pseudocode, flowchart and testing plan

## Working
## Pseudocode
START
Load 100 questions
Set required quiz size
Randomly select required number of unique questions
Set score = 0
FOR each selected question
    Display question and options
    Read answer
    IF answer is correct
        Increase score
    ELSE
        Display correct answer
END FOR
Display final score and correct-answer count
END
## Flowchart
START → Load 100 Questions → Set Quiz Size → Randomly Select Unique Questions → Display Question → Input Answer → Correct?
→ YES → Add Score → More Questions?
→ NO → Show Correct Answer → More Questions?
→ YES → Display Question
→ NO → Display Final Score → END

## Project Coverage
Control flow, functions, Boolean values/operators, lists, tuples, sets, dictionaries, list operations, randomization, GCD, prime numbers/factors, Fibonacci, powers, pseudocode, flowcharts and basic algorithm analysis.
