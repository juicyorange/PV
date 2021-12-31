/* 
별찍기.
예시 : 
input : 5
reulst :
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
*/
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
let num = Number(input);

let result = "";
let tempResult = "";
for (let i = 0; i < num; i++) {
  for (let j = 0; j < num * 2 - i - 1; j++) {
    if (i > j) {
      result += " ";
    } else {
      result += "*";
    }
  }
  result += "\n";
}
for (i = num - 2; i >= 0; i--) {
  for (j = 0; j < num * 2 - i - 1; j++) {
    if (i > j) {
      result += " ";
    } else {
      result += "*";
    }
  }
  result += "\n";
}
console.log(result);
