// There is a special syntax called the rest parameter syntax to create
// a function that accepts any number of arguments

function sum(...values) {
    let sum = 0;
    for (let i = 0; i < values.length; i++) {
        sum += values[i];
    }

    return sum;
}
console.log(sum(1));
console.log(sum(1, 2));
console.log(sum(1, 2, 3));
console.log(sum(1, 2, 3, 4));