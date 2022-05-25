Problem 

An operator has been making configuration changes without committing the con-
figurations. When a second operator makes a different configuration change and
commits, that second operator will be committing both configurations. Problems
ensue.

Solution 

Run a job that does a rollback if there is a candidate configuration,
preventing this issue from occurring