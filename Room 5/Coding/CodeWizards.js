function deepClone(obj) {
    if (obj === null || typeof obj !== "object") {
        return obj;
    }

    if (Array.isArray(obj)) {
        return obj.map(item => deepClone(item));
    }

    const clonedObj = {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            clonedObj[key] = deepClone(obj[key]);
        }
    }
    return clonedObj;
}

const original = {
    a: 1,
    b: {
        c: 2,
        d: [3, 4]
    }
};

const copy = deepClone(original);
copy.b.d.push(5);

console.log(original); 
console.log(copy);
