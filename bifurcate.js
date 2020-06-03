// This snippet splits values into two groups and then puts a truthy
// element of filter in the first group, and in the second group otherwise.

const bifurcate = (arr, filter) =>
    arr.reduce((acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc), [
        [],
        []
    ]);
bifurcate(['beep', 'boop', 'foo', 'bar'], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]