function typeWriter(eid, txt, iterator) {
    if (iterator < txt.length) {
        document.getElementById(eid).innerHTML += txt.charAt(iterator);
        iterator++;
    } else {
        document.getElementById(eid).innerHTML = '';
        iterator = 0;
    }
    setTimeout(function() { typeWriter(eid, txt, iterator) }, 250);
}