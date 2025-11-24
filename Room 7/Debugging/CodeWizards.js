//Fix the async function to correctly handle the returned string.

async function getData() {
    return "data";
  }
  
  async function useData() {
    const response = getData();
    console.log(await response.json());
  }
  