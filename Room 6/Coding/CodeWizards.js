function delay(ms) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(`Resolved after ${ms} ms`);
        }, ms);
    });
}


delay(1000).then(message => console.log(message));

