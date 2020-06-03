// This snippet splits values into two groups, based on a predicate function.
// If the predicate function returns a truthy value, the element will be placed 
// in the first group. Otherwise, it will be placed in the second group.

const bifurcateBy = (arr, fn) =>
    arr.reduce((acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc), [
        [],
        []
    ]);

bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b');
// [ ['beep', 'boop', 'bar'], ['foo'] ]