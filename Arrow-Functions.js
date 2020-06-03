const func = () => { return 'something'; }
func();
// OR
const func = () => 'something';
// OR WITH PARAM (SINGLE)
func();
const func = arg => {
    console.log(arg);
}
func('hello');
// OR WITH MULTI PARAMS
const func = (arg, arg1) => {
    console.log('arg: ', arg);
    console.log('arg1: ', arg1);
};

func('hello', 'there');