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
