// This snippet can be used to find out the time it takes to execute a function.

const timeTaken = callback => {
    console.time('timeTaken');
    const r = callback();
    console.timeEnd('timeTaken');
    return r;
};

timeTaken(() => Math.pow(2, 10)); // 1024, (logged): timeTaken: 0.02099609375ms