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
