$(document).ready(function(){
    $('.sidenav').sidenav();
});

window.onscroll = function() {scrollfunc()};

function scrollfunc() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}

// postlist, posts(id: blog-i), mobile-demo
function loadIndex() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var dataObj = JSON.parse(this.responseText);
      var i =0;
      titles = dataObj['Title'];
      descriptions = dataObj['Description'];
      HTMLcontent1 = "";
      HTMLcontent2 = "";
      while(typeof titles[i] !== "undefined")
      {
        HTMLcontent1 += '<li class="w3-hover-green w3-border-top w3-border-bottom w3-border-white"><a class="w3-text-white" href="/?q='+i+'">'+titles[i]+'</a></li>'
        HTMLcontent2 += '<li class="w3-padding-16 w3-hover-green">'+
          '<a href="/?q='+i+'"><span class="w3-large">'+titles[i]+'</span><br><span>'+descriptions[i]+'</span></a>'+
        '</li>'
        i ++;
      }
     document.getElementById("mobile-demo").innerHTML += HTMLcontent1;
     document.getElementById("postlist").innerHTML += HTMLcontent2;
    }
  };
  xhttp.open("GET", "data/data.json", true);
  xhttp.send();
}

function loadBlogs(start=0){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var dataObj = JSON.parse(this.responseText);
      var i =0;
      titles = dataObj['Title'];
      descriptions = dataObj['Description'];
      codes = dataObj['Code'];
      HTMLcontent = "";
      while(typeof titles[start+i] !== "undefined" && i<3)
      {
        HTMLcontent += '<div class="w3-card-4 w3-margin w3-black">'+
        '<div class="w3-container">'+
        '<h3><b>'+titles[start+i]+'</b></h3>'+
        '<h5>'+descriptions[start+i]+'</h5>'+
        '</div>'+
        '<div class="w3-container">'+
        '<pre class="code">'+codes[start+i]+'</pre>'+
        '</div>'+
        '</div>'
        i ++;
        if(typeof titles[start+i] == "undefined"){
          document.getElementById("loadBtn").disabled = true;
          document.getElementById("loadBtnMob").disabled = true;
        }
      }
     document.getElementById("posts").innerHTML += HTMLcontent;
     loaded += 3;
    }
  };
  xhttp.open("GET", "data/data.json", true);
  xhttp.send();
}
loadIndex();
var params = new URLSearchParams(location.search);
var q = params.get('q')
if (q == null){
  var loaded = 0;
  loadBlogs(loaded);
}
else
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var dataObj = JSON.parse(this.responseText);
      titles = dataObj['Title'];
      descriptions = dataObj['Description'];
      codes = dataObj['Code'];
      HTMLcontent = "";
      HTMLcontent += '<div class="w3-card-4 w3-margin w3-black">'+
      '<div class="w3-container">'+
      '<h3><b>'+titles[q]+'</b></h3>'+
      '<h5>'+descriptions[q]+'</h5>'+
      '</div>'+
      '<div class="w3-container">'+
      '<pre class="code">'+codes[q]+'</pre>'+
      '</div>'+
      '</div>'
     document.getElementById("posts").innerHTML += HTMLcontent;
    }
  };
  xhttp.open("GET", "data/data.json", true);
  xhttp.send();
  document.getElementById("loadBtn").disabled = true;
  document.getElementById("loadBtnMob").disabled = true;
}
