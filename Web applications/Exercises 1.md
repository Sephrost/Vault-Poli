# Exercise 1: Better Scores
_Goal: basic handling of JavaScript arrays_

Develop a small JavaScript program to manage the scores given to your user in a question-and-answer website (e.g., StackOverflow). Scores are integer numbers, and they may be negative. You should:
 
- Define an array with all the scores you received in chronological order. For the moment:
  - Embed the scores directly in the source code.
  - Ignore the question, answer, and date that generated the score.
- Duplicate the array, but:
  - Eliminate all negative scores (call `NN` the number of negative scores that are deleted).
  - Eliminate the two lowest-ranking scores.
  - Add `NN+2` new scores, at the end of the array, with a value equal to the (rounded) average of the existing scores.
- Print both arrays, comparing the scores before and after the "improvement," and showing the averages in both cases.

```javascript
"use strict";

const grades = [12, -5, 14, 17, 52];
console.log(grades);

let grades_copy = Array.from(grades);
let avg = 0; let count = 0; let neg = 2;

grades_copy = grades_copy.filter(function (grade) {
  if (grade < 0) {
    neg++;
    return false;
  }

  avg += grade; count++;
  return true;
});

grades_copy.sort();
grades_copy.splice(0, 2);

while (neg--) {
  grades_copy.push(avg / count);
}
console.log(grades_copy);
```
# Exercise 2: My Users' List
_Goal: basic handling of JavaScript strings_

Develop a small JS program to manage the list of users in a Q&A website.

- Define the names of users as a comma-separated list.
 - For instance: "Luigi De Russis, Luca Mannella, Fulvio Corno, Juan Pablo Saenz Moreno, Enrico Masala, Antonio Servetti"
- Parse the string and create an array containing one name per array position.
 - Beware: no extra spaces should be present.
- Create a second array by computing the acronyms of the people as the initial letters of the name. Acronyms should be in all-capital letters.
 - For example, Luigi De Russis -> LDR.
- Print the resulting list of acronyms and the full names.
 - Extra: in alphabetical order of acronym.
```javascript
"use strict";

const src = "Luigi De Russis, Luca Mannella, Fulvio Corno, Juan Pablo Saenz Moreno, Enrico Masala, Antonio Servetti"

let ll = src.split(',').map((s) => s.trim())
let ll_copy = Array.from(ll)

ll_copy = ll_copy.map((s) => s = s.split(' ').map((s) => s[0]).join(''));
console.log(ll_copy)
```
# Exercise 3: Q&A
_Goal: managing a simple data structure as an array of objects_.

Using JavaScript objects and functional programming methods, manage objects that contain information about a question and their answers.

Each answer will contain:

- Response (text)
- Respondent name
- Score (integer number, positive or negative)
- Date

Define a constructor function `Answer` to create one or more answers.

A question, instead, is made of:

- Question (text)
- Questioner name
- Date
- List of answers

Define a constructor function `Question` to represent a question. Implement the following methods to manipulate its answers: 

- `add(answer)` // pass a fully-constructed `Answer` object
- `findAll(name)` // returns all the Answers of a given respondent
- `afterDate(date)` // returns an array of Answers after the given date
- `listByDate()` // returns an array of Answers, sorted by increasing date
- `listByScore()` // same as before, by decreasing score

Create an instance of `Question` with at least four `Answer`s in it and test the previous methods.
```javascript
`use strict`;

let answer = function (response, respondant, score, date) {
  this.response = response,
    this.respondant = respondant,
    this.score = score,
    this.date = date
};

let a1 = new answer("test", "Me", 5, new Date(2020, 2, 1));
let a2 = new answer("test", "You", 5, new Date(2020, 1, 1));

const question = function (question, questioner, date) {
  this.question = question,
    this.questioner = questioner,
    this.date = date,
    this.answers = []
  this.add = (answer) => this.answers.push(answer);
  this.findall = respondant => this.answers.filter((a) => respondant === a.respondant);
  this.afterDate = date => this.answers.filter((a) => date < a.date);
  this.listByDate = () => Array.from(this.answers).sort((a, b) => a.date - b.date);
  this.listByScore = () => Array.from(this.answers).sort((a, b) => a.score - b.score);
}

let q1 = new question("What is your name?", "You", new Date(2020, 1, 1));
q1.add(a1);
q1.add(a2);

console.log(q1.listByDate());
```