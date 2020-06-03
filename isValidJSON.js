// This snippet can be used to check whether a string is a valid JSON.

const isValidJSON = str => {
    try {
        JSON.parse(str);
        return true;
    } catch (e) {
        return false;
    }
};

isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // true