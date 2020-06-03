// Sometimes, we need to check if a variable exists or if it has a valid value, 
// to consider them as a true value. For this kind of validation, 
// you can use the !! (double-negation operator).
// A simple !!variable, which will automatically convert any kind of data to a
// boolean and this variable will return false only if it has some of these 
// values: 0, null, "", undefined, or NaN, otherwise, it will return true.

class Account(cash) {
    this.cash = cash;
    this.hasMoney = !!cash;
}

var account = new Account(100.50);
console.log(account.cash); // 100.50
console.log(account.hasMoney); // true

var emptyAccount = new Account(0);
console.log(emptyAccount.cash); // 0
console.log(emptyAccount.hasMoney); // false