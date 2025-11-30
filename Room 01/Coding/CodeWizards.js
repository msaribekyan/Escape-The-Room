// Write a function sumEven() that returns the sum of even numbers from 1 to 10.


function sumEven() {
  let sum = 0;
  for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
      sum += i;
    }
  }
  return sum;
}

console.log(sumEven());
