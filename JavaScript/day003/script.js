/*

Perform a search and replace on the sentence using the arguments provided and return the new sentence.

*/

function myReplace(str, before, after) {
  if (before.charAt(0) === before.charAt(0).toUpperCase()) {
    return str.replace(before, after.charAt(0).toUpperCase() + after.slice(1));
  } else {
    return str.replace(before, after);
  }
}

// console.log(
//   myReplace("A brown fox jumped over the lazy dog", "jumped", "leaped")
// );
// console.log(myReplace("He is Sleeping on the couch", "Sleeping", "sitting"));

/*

Find the missing letter in the passed letter range and return it.

*/
function fearNotLetter(str) {
  let alfabet = "abcdefghijklmnopqrstuvwxyz";
  let firstLetter = str.charAt(0);
  let lastLetter = str.slice(-1);
  let range = alfabet.slice(
    alfabet.indexOf(firstLetter),
    alfabet.indexOf(lastLetter)
  );

  for (let i = 0; i <= range.length; i++) {
    if (str[i] !== range[i]) {
      return range[i];
    }
  }
}

// console.log(fearNotLetter("abce"));
// console.log(fearNotLetter("stvwx"));
// console.log(fearNotLetter("abcdefghijklmnopqrstuvwxyz"));
// console.log(fearNotLetter("bcdf"));
// console.log(fearNotLetter("abcdefghjklmno"));

/*

Write a function that takes two or more arrays and returns a new array
of unique values in the order of the original provided arrays.
In other words, all values present from all arrays should be included
in their original order, but with no duplicates in the final array.

*/

function uniteUnique(...arr) {
  let args = [...arr];
  let newArr = [];

  for (let i = 0; i < args.length; i++) {
    for (let j = 0; j < args[i].length; j++) {
      if (!newArr.includes(args[i][j])) {
        newArr.push(args[i][j]);
      }
    }
  }

  return newArr;
}

// console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]));
// console.log(uniteUnique([1, 2, 3], [5, 2, 1]));
// console.log(uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]));
