var it_works = false;

jQuery.ajax({
    type: "POST",
    url: 'some_file.php',
    success: function(data) {
        it_works = true;
    },
    async: false // <- this turns it into synchronous
});

// Execution is BLOCKED until request finishes.

// it_works is available
alert(it_works);