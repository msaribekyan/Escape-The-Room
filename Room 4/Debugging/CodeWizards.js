//Fix the code to correctly filter positive numbers.
  
  function filterPositives(arr) {
    return arr.map(num => num > 0);
  }
  
  console.log(filterPositives([-1, 2, -3, 4]));
  