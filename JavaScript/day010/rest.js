function sum(...rest) {
  let sum = 0;
  for (let i = 0; i < rest.length; i++) {
    sum += rest[i];
  }
  console.log(sum);
  return sum;
}
sum(1, 2, 3);
sum(1, 2, 3, 4);
