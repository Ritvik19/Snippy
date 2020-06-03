// This snippet can be used to convert a nodeList to an array.

const nodeListToArray = nodeList => [...nodeList];

nodeListToArray(document.childNodes); // [ <!DOCTYPE html>, html ]