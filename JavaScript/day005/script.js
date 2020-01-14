// 16:43 - start

// Intermediate Algorithm Scripting: Smallest Common Multiple

function smallestCommons(arr) {
  let max = Math.max(arr[0], arr[1]);
  let min = Math.min(arr[0], arr[1]);
  let multiply = max;

  for (let i = max; i >= min; i--) {
    if (multiply % i !== 0) {
      multiply = multiply + max;
      i = max;
    }
  }
  return multiply;
}

// console.log(smallestCommons([1, 5]));
// console.log(smallestCommons([5, 1]));
// console.log(smallestCommons([23, 18]));

// Drop it
// Given the array arr, iterate through and remove each element starting from the
// first element (the 0 index) until the function func returns true when the
// iterated element is passed through it.

function dropElements(arr, func) {
  let times = arr.length;
  for (let i = 0; i < times; i++) {
    if (func(arr[0])) {
      break;
    } else {
      arr.shift();
    }
  }

  return arr;
}

// console.log(
//   dropElements([1, 2, 3], function(n) {
//     return n < 3;
//   })
// );
// console.log(
//   dropElements([1, 2, 3, 4], function(n) {
//     return n > 5;
//   })
// );

// console.log(
//   dropElements([0, 1, 0, 1], function(n) {
//     return n === 1;
//   })
// );

// console.log(
//   dropElements([1, 2, 3, 9, 2], function(n) {
//     return n > 2;
//   })
// );

// Flatten a nested array. You must account for varying levels of nesting.
function steamrollArray(arr) {
  // I'm a steamroller, baby
  return arr.flat(Infinity);
}

// console.log(steamrollArray([1, [2], [3, [[4]]]]));

// Binary Agents
// Return an English translated sentence of the passed binary string.
function binaryAgent(str) {
  let strArr = str.split(" ");
  let newStr = "";
  for (let i = 0; i < strArr.length; i++) {
    let letter = String.fromCharCode(parseInt(strArr[i], 2).toString(10));
    newStr = newStr + letter;
  }

  return newStr;
}

// console.log(
//   binaryAgent(
//     "01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"
//   )
// );

// Everything Be True
function truthCheck(collection, pre) {
  return collection.every(obj => obj[pre]);
}

//true
// console.log(
//   truthCheck(
//     [
//       { user: "Tinky-Winky", sex: "male" },
//       { user: "Dipsy", sex: "male" },
//       { user: "Laa-Laa", sex: "female" },
//       { user: "Po", sex: "female" }
//     ],
//     "sex"
//   )
// );
