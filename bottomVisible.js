// This snippet checks whether the bottom of a page is visible.

const bottomVisible = () =>
    document.documentElement.clientHeight + window.scrollY >=
    (document.documentElement.scrollHeight || document.documentElement.clientHeight);

bottomVisible(); // true