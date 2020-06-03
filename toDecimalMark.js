// This snippet uses the toLocaleString() function to convert 
// float-point arithmetic to the decimal mark form by using a
// number to make a comma-separated string.

const toDecimalMark = num => num.toLocaleString('en-US');

toDecimalMark(12305030388.9087); // "12,305,030,388.909"