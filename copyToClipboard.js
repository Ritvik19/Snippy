function copyToClipboard(containerid) {
    var el = document.getElementById(containerid);
    var range = document.createRange();
    range.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    document.execCommand('copy');
    return false;
}