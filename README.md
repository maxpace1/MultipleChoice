# MultipleChoice
A simple script to find the answer to multiple choice questions by querying through Google search.

To add a question, edit the questions list following the format:
```
(
  "<Question>",
  ["<Option1>", "<Option2>", "<Option3>", "<Option4>"]
),...
   ```

### Background
This project was the result of inspiration from other bots and scripts to answer questions to various trivia games, namely HQ Trivia.
While my own attempt at this goal came much later than HQ Trivia, my desire to make a multiple-choice solver lingered.
After a few different approaches to the task, I settled on the current simple yet reasonably effective approach.

### Limitations
This algorithm runs by querying Google with the question and observing how frequently the provided options appear. Because of this, many styles of questions will not work well.
For example, numerical questions subject to any rounding or imprecision will likely not be successfully answered, nor will questions with any subjectivity.
It may struggle with questions where a possible answer could be phrased in other ways or may go by other names.

More generally, tbe questions where the algorithm will find success are simple trivia questions with definitive, unambiguous, non-numerical, and brief answers.
