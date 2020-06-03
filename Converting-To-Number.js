// A simple +variable, but it only works with string numbers, otherwise, it will return NaN (Not a Number).

function toNumber(strNumber) {
    return +strNumber;
}
console.log(toNumber("1234")); // 1234
console.log(toNumber("ACB")); // NaN
// This magic will work with Date too and, in this case, it will return the timestamp number:
console.log(+new Date()) // 1461288164385