// This snippet gets a number as input and returns an array of its digits.

const digitize = n => [...
    `${n}`
].map(i => parseInt(i));

digitize(431); // [4, 3, 1]