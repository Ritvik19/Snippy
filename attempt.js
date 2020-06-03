// This snippet executes a function, returning either the result or the caught error object.

const attempt = (fn, ...args) => {
    try {
        return fn(...args);
    } catch (e) {
        return e instanceof Error ? e : new Error(e);
    }
};
var elements = attempt(function(selector) {
    return document.querySelectorAll(selector);
}, '>_>');
if (elements instanceof Error) elements = []; // elements = []