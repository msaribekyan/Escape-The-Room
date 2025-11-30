// Write a function that takes an object that may contain nested objects and returns a new object where the nesting is flattened. Each key should represent its path using a dot (.) to separate levels.

// Note: You may need to use recursion.



function flattenObject(obj, parentKey = '', result = {}) {
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            const newKey = parentKey ? `${parentKey}.${key}` : key;
            if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
                flattenObject(obj[key], newKey, result);
            } else {
                result[newKey] = obj[key];
            }
        }
    }
    return result;
}

const profile = {
    user: {
        name: {
            first: "Jane",
            last: "Doe"
        },
        age: 28
    }
};

console.log(flattenObject(profile));
