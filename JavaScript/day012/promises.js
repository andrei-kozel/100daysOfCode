const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("Timeout");
    resolve("Hi from promise");
  }, 2000);
});

console.log("I am after promise");

promise.then(data => console.log(data)).catch(e => console.log(e));

console.log("wait ....");
