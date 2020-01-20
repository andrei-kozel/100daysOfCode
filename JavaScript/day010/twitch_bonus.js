function getBonus() {
  if (document.querySelector(".tw-button")) {
    document.querySelector(".tw-button").click();
    console.log("+ bonus");
  }
  console.log("not bonus");
}

setInterval(getBonus, 60 * 1000);
