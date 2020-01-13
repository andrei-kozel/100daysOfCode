// Replace Loops using Recursion
// from freecodecamp.org

function sum(arr, n) {
  if (n <= 0) {
    return arr[0];
  } else {
    return sum(arr, n - 1) + arr[n];
  }
}

console.log(sum([1], 0));
console.log(sum([2, 3, 4], 1));

console.log("--------------------------------");

// Use Recursion to Create a Countdown
// freecodecamp.org

function countdown(n) {
  if (n < 1) {
    return [];
  } else {
    const countArr = countdown(n - 1);
    countArr.unshift(n);
    return countArr;
  }
}

console.log(countdown(6));
console.log(countdown(10));

console.log("--------------------------------");

// Use Recursion to Create a Range of Numbers
// freecodecamp.org

function rangeOfNumbers(startNum, endNum) {
  if (startNum === endNum) {
    return [startNum];
  } else {
    const newArr = rangeOfNumbers(startNum + 1, endNum);
    newArr.unshift(startNum);
    return newArr;
  }
}

console.log(rangeOfNumbers(1, 5));
console.log(rangeOfNumbers(6, 9));

console.log("--------------------------------");

// Use Destructuring Assignment to Extract Values from Objects
// freecodecamp.org

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};
const { today, tomorrow, yesterday } = HIGH_TEMPERATURES;

console.log(yesterday); // should be 75
console.log(today); // should be 77
console.log(tomorrow); // should be 80

console.log("--------------------------------");

// Complete a Promise with resolve and reject
// freecodecamp.org

// const makeServerRequest = new Promise((resolve, reject) => {
//   // responseFromServer represents a response from a server
//   let responseFromServer ;

//   if (responseFromServer) {
//     resolve("We got the data");
//   } else {
//     reject("Data not received");
//   }
// });
