function capitalizeStrings(obj) {
  const result = {};
  for (const key in obj) {
    if (typeof obj[key] === 'string') {
      result[key] = obj[key].toUpperCase();
    } else {
      result[key] = obj[key];
    }
  }
  return result;
}


const input = { name: "anna", age: 25, city: "paris" };
const output = capitalizeStrings(input);
console.log(output);


