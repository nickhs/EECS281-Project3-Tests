# EECS 281 Community Test Cases

This is a repository of shared test cases for 281 projects. It includes a test
runner (`run_tests.py`) and a number of test cases in `tests` and their relevant
output in `output`. `tests.json` is the glue that sticks the parts together.

If you use these tests and spot a misssing edge case consider adding it in to
the repo!

# Quickstart

Clone this repository:

    git clone https://github.com/nickhs/EECS281-Project3-Tests

Run the tests:

    python run_tests.py my_program_executable

Where `my_program_executable` is the location of your program.

# Contributing

Make your changes to the repository and submit a
pull request. Someone will look at it shortly and
merge it in!

## Step One

Add your test cases to the `tests` folder. Name it something unique.

## Step Two

Add the test case output to the `output` folder. Name it the same
thing you named your test case so others can track it down easier.

## Step Three

Add your new test case to tests.json by adding it in the `tests` block.
Make sure it includes the following information:

    "test1": { // the name of the test, make this unique
        "email": "nickhs@umich.edu", // your email address
        "added": "27-Oct-2013", // the date it was added (today's date)
        "test": "-v 100 -c PAIRING tests/test-4-PAIRING.txt", // the relevant flags and path to the test case
        "output": "output/test-4-PAIRING.txt" // the path to the output
    },

## Step Four

Test it. Run `run_tests.py` and make sure everything appears to be working.

## Step Five

Submit a pull request back to the repository. Pat yourself on the back, you're a saint..

# FAQ

1) One of these test cases is incorrect? How do I remove it?

    Open up an issue and we'll get right into looking into it.

2) How do I know someone won't steal my tests?

    It's against the Engineering Honour Code to submit a test case
    that is not original (i.e. not yours) to the autograder.
    Git/Github does all the book keeping for us on who submitted what
    that we can turn over to the honour council if required.

    Please do NOT submit tests cases that aren't yours. We do reserve
    the right to report any and all suspected honour code violations.

3) It told me to report an issue - what do I do?

    Open a Github issue and we'll look into it right away. Let us know
    what output you got from `run_tests.py` and make sure you're on latest!

4) If you submit or use these test cases are you infringing on the honour code?

    Short answer is probably not.

    Long answer, these are the rules (from Piazza post 970):

        Just to reiterate the groundrules:

        * the code you turn in for grading must be entirely your own, and you should take care to keep it private and not show it to anyone except EECS 281 instructional staff

        * the test cases that you turn in for grading must be your own, but you are welcome to share test cases (with other students you trust to be honest and not claim them as their own and turn them in themselves)

        * you are allowed (and encouraged) to help each other, discuss project specifications, relative merits of alternative solutions, pretty much anything so long as it doesn't get so specific as to details of actual graded project code

        * you are allowed (and encouraged) to discuss and share program output if that helps you to understand or debug your project (both individually or on Piazza)

        * you are allowed (and encouraged) to discuss and share small examples of code to illustrate a general idea, so long as it isn't actual code that will go in your project (both individually or on Piazza)

        - Don Winsor

    The second point being the most salient. It's your call.
