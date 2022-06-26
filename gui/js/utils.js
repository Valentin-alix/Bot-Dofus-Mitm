function sleep(milliseconds) {
  const start = Date.now();
  while (Date.now() - start < milliseconds);
}

function redirect(page = "home.html") {
  sleep(180);
  document.location.href = page;
}
