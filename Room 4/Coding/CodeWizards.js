// Write a function that flattens a nested array (only one level - no deeply nested flattening).


function flattenArray(arr) {
  return arr.flat();

const nested = [1, [2, 3], 4, [5, 6]];
console.log(flattenArray(nested));
