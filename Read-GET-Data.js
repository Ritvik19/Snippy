// www.example.com?q=something

var params = new URLSearchParams(location.search);
var q = params.get('q')
if (q == null) {

} else if (q == 'something') {

} else {

}