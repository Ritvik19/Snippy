// Longhand:
const fruits = ['mango', 'peach', 'banana'];
for (let i = 0; i < fruits.length; i++) {}

// Shorthand:
for (let fruit of fruits) {}

// If you just wanted to access the index, do:
for (let index in fruits) {}

// This also works if you want to access keys in a literal object:
const obj = { continent: 'Africa', country: 'Kenya', city: 'Nairobi' }
for (let key in obj)
    console.log(key) // output: continent, country, city