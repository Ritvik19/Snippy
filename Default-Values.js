// Today, in ES6, there is the default argument feature. To simulate 
// this feature in old browsers, you can use the || (OR operator) by
// including the default value as a second parameter to be used.
// If the first parameter returns false, the second one will be used as a default value. 

function User(name, age) {
    this.name = name || "Oliver Queen";
    this.age = age || 27;
}
var user1 = new User();
console.log(user1.name); // Oliver Queen
console.log(user1.age); // 27
var user2 = new User("Barry Allen", 25);
console.log(user2.name); // Barry Allen
console.log(user2.age); // 25