// Write a function that accepts an array of objects and returns a new array sorted by a specific numeric key.

function sortByNumericKey(arr, key) {
  return [...arr].sort((a, b) => a[key] - b[key]);
}


const data = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 20 },
  { name: "Charlie", age: 30 }
];

const sortedByAge = sortByNumericKey(data, "age");
console.log(sortedByAge);
