// 18:17 start
function rot13(str) {
  let alphabet = "abcdefghijklmnopqrstuvwxyz".toUpperCase();
  let convertedString = "";

  for (let letterPosition = 0; letterPosition < str.length; letterPosition++) {
    let index = alphabet.indexOf(str[letterPosition]);
    if (index >= 0 && index <= 12) {
      convertedString = convertedString + alphabet[index + 13];
    } else if ((index > 12) & (index <= 26)) {
      convertedString = convertedString + alphabet[index - 13];
    } else {
      convertedString = convertedString + str[letterPosition];
    }
  }
  return convertedString;
}

// Change the inputs below to test
console.log(rot13("SERR PBQR PNZC")); // FREE CODE CAMP
console.log(rot13("SERR CVMMN!")); // FREE PIZZA!
