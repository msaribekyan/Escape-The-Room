//Fix the chaining Promises.

function fetchData() {
    return Promise.resolve("data");
  }
  fetchData().then(console.log("Done"));
  