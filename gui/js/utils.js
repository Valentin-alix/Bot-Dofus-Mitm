function sleep(milliseconds) {
  const start = Date.now();
  while (Date.now() - start < milliseconds);
}

function redirect(page = "home.html") {
  document.location.href = page;
}
