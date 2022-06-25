function sleep(milliseconds) {
  const start = Date.now();
  while (Date.now() - start < milliseconds);
}

function redirect(page = "home.html") {
  document.location.href = page;
}

// FIXME BUG WHEN CHANGING QUICKLY PAGE
window.onload = function () {
  for (anchor of document.getElementsByTagName("a")) {
    anchor.addEventListener(
      "click",
      function (event) {
        event.preventDefault();
        sleep(180);
        redirect(this.href);
      },
      false
    );
  }
};
