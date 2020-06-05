function loadCode() {
    var xhttp = new XMLHttpRequest();
    var filepath = '../../..'
    console.log(filepath)
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            col1 = dataObj['col1']
            content = ''
            var i = 0;
            while (typeof col1[i] !== "undefined") {
                content += col1[i] + '\n'
            }
            document.getElementById("demo").innerHTML = content;
        }
    };
    xhttp.open("GET", filepath, true);
    xhttp.send();
}