$(document).ready(function() {
    $(".sidenav").sidenav();
});

window.onscroll = function() {
    scrollfunc();
};

function scrollfunc() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById("myBar").style.width = scrolled + "%";
}

// postlist, posts(id: blog-i), mobile-demo
function loadIndex() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            var i = 0;
            titles = dataObj["Title"];
            descriptions = dataObj["Description"];
            HTMLcontent1 = "";
            HTMLcontent2 = "";
            while (typeof titles[i] !== "undefined") {
                HTMLcontent1 +=
                    '<li class="w3-hover-green w3-border-top w3-border-bottom w3-border-white"><a class="w3-text-white" href="/?q=' +
                    i +
                    '">' +
                    titles[i] +
                    "</a></li>";
                HTMLcontent2 +=
                    '<a href="/?q=' +
                    i +
                    '"><li class="w3-padding w3-hover-green w3-border-top w3-border-bottom w3-border-white">' +
                    '<span class="w3-large">' +
                    titles[i] +
                    "</span><br><span>" +
                    descriptions[i] +
                    "</span>" +
                    "</li></a>";
                i++;
            }
            document.getElementById("mobile-demo").innerHTML += HTMLcontent1;
            document.getElementById("postlist").innerHTML += HTMLcontent2;
            document.getElementById("total").innerHTML = i;
            document.getElementById("total-m").innerHTML = i;
        }
    };
    xhttp.open("GET", "data/data.json", true);
    xhttp.send();
}

function loadBlogs(loaded = 0) {
    upperlim = 3;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            var i = 0;
            titles = dataObj["Title"];
            descriptions = dataObj["Description"];
            codes = dataObj["Code"];
            meta = dataObj["Meta"];
            HTMLcontent = "";
            while (typeof titles[loaded + i] !== "undefined" && i < upperlim) {
                HTMLcontent +=
                    '<div class="w3-card-4 w3-margin w3-black">' +
                    '<div class="w3-container">' +
                    "<h3><b>" +
                    titles[loaded + i] +
                    "</b></h3>" +
                    "<h5>" +
                    descriptions[loaded + i] +
                    "</h5>" +
                    "</div>" +
                    '<div class="w3-container">' +
                    '<pre class="code">' +
                    codes[loaded + i] +
                    "</pre>" +
                    "</div>" +
                    "</div>";
                i++;
                if (typeof titles[loaded + i] == "undefined") {
                    document.getElementById("loadBtn").disabled = true;
                    document.getElementById("loadBtnMob").disabled = true;
                }
            }
            document.getElementById("posts").innerHTML += HTMLcontent;
        }
    };
    xhttp.open("GET", "data/data.json", true);
    xhttp.send();
    return loaded + upperlim;
}
loadIndex();
var params = new URLSearchParams(location.search);
var q = params.get("q");
if (q == null) {
    var loaded = loadBlogs(0);
} else {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            titles = dataObj["Title"];
            descriptions = dataObj["Description"];
            codes = dataObj["Code"];
            meta = dataObj["Meta"];
            HTMLcontent = "";
            HTMLcontent +=
                '<div class="w3-card-4 w3-margin w3-black">' +
                '<div class="w3-container">' +
                "<h3><b>" +
                titles[q] +
                "</b></h3>" +
                "<h5>" +
                descriptions[q] +
                "</h5>" +
                "</div>" +
                '<div class="w3-container">' +
                '<pre class="code">' +
                codes[q] +
                "</pre>" +
                "</div>" +
                "</div>";
            document.getElementById("posts").innerHTML += HTMLcontent;
        }
    };
    xhttp.open("GET", "data/data.json", true);
    xhttp.send();
    document.getElementById("loadBtn").disabled = true;
    document.getElementById("loadBtnMob").disabled = true;
}

function postFilter(inputEl, listEl, element) {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById(inputEl);
    filter = input.value.toUpperCase();
    ul = document.getElementById(listEl);
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName(element)[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}