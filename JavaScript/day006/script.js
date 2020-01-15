// Roman Numeral Converter
// Convert the given number into a roman numeral.

function convertToRoman(num) {
  let romanCombos = [
    { number: 1000, romanNumber: "M" },
    { number: 900, romanNumber: "CM" },
    { number: 500, romanNumber: "D" },
    { number: 400, romanNumber: "CD" },
    { number: 100, romanNumber: "C" },
    { number: 90, romanNumber: "XC" },
    { number: 50, romanNumber: "L" },
    { number: 40, romanNumber: "XL" },
    { number: 10, romanNumber: "X" },
    { number: 9, romanNumber: "IX" },
    { number: 5, romanNumber: "V" },
    { number: 4, romanNumber: "IV" },
    { number: 1, romanNumber: "I" }
  ];
  let roman = "";

  for (let i = 0; i < romanCombos.length; i++) {
    if (num / romanCombos[i].number >= 1) {
      roman =
        roman +
        romanCombos[i].romanNumber.repeat(
          Math.floor(num / romanCombos[i].number)
        );
      num =
        num - Math.floor(num / romanCombos[i].number) * romanCombos[i].number;
    }
  }

  return roman;
}
