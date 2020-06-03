// The rest operator allows an indefinite number of arguments, represented as an array.


function add(...nums) {
    return sum(...nums);
}

add(1, 2, 3, 4, 5);
add(1, 3);
add(4, 5, 3, 4);