// Write a function that chains two Promises together manually without using Promise.all().
// Team name: teamX
// Topic: Manual Promise chaining

function chainPromises(promise1, promise2) {
  return promise1
    .then(result1 => {
      console.log("First promise resolved:", result1);
      return promise2(result1);
    .then(result2 => {
      console.log("Second promise resolved:", result2);
      return result2;
    })
    .catch(error => {
      console.error("Error in promise chain:", error);
    });
}

const p1 = new Promise((resolve, reject) => {
  setTimeout(() => resolve(5), 1000);
});

const p2 = (prevResult) => new Promise((resolve, reject) => {
  setTimeout(() => resolve(prevResult * 2), 1000);
});

chainPromises(p1, p2);
