function go(e) {
    if (e.keyCode === 13) {
        e.preventDefault(); // Ensure it is only this code that rusn
        alert("Enter was pressed");
    }
}

//call: go(event)