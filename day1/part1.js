/*

https://adventofcode.com/2023/day/1

From when I was doing this in javascript, RIP to part 2, gone but never forgotten

*/

const fs = require("node:fs");

function isNumeric(char) {
  return /^\d+$/.test(char);
}

fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) {
    console.log("Error reading file: " + err);
    return;
  }
  let lines = data.split("\n");
  let total = 0;
  lines.forEach((line) => {
    let nums = [];
    for (const char of line) {
      if (isNumeric(char)) {
        nums.push(char); // Push as chars, not ints
      }
    }

    let first = nums[0];
    let last = nums[nums.length - 1];
    let count = first + last; // As both are characters, "adding them togther" make 7+7 = 77

    total += parseInt(count);
    console.log("%d %s", count, line);
  });
  console.log(total);
});
