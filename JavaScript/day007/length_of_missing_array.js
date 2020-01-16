// You get an array of arrays.
// If you sort the arrays by their length, you will see, that their length-values are consecutive.
// But one array is missing!
// You have to write a method, that return the length of the missing array.

function getLengthOfMissingArray(arrayOfArrays) {
  let sortedArray = [];
  if (arrayOfArrays === null) {
    return 0;
  } else {
    sortedArray = arrayOfArrays.sort(function(a, b) {
      if (a == null || b == null) {
        return 0;
      } else {
        return a.length - b.length;
      }
    });
  }

  console.log(sortedArray);

  for (let index = 0; index < sortedArray.length; index++) {
    if (sortedArray[index] !== null || sortedArray[index + 1] !== null) {
      if (sortedArray[index + 1].length - sortedArray[index].length > 1) {
        return sortedArray[index].length + 1;
      }
    }
  }
}

// console.log(
//   getLengthOfMissingArray([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]])
// );
// console.log(
//   getLengthOfMissingArray([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]])
// );
console.log(getLengthOfMissingArray([[[1, 2, 2], null]]));
// console.log(
//   getLengthOfMissingArray([
//     ["a", "a", "a"],
//     ["a", "a"],
//     ["a", "a", "a", "a"],
//     ["a"],
//     ["a", "a", "a", "a", "a", "a"]
//   ])
// );
