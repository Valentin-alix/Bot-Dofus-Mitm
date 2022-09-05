function play_item(item_name) {
  eel.play_item(item_name);
  console.log(document.querySelectorAll(".user_action"));
  for (button of document.querySelectorAll(".user_action")) {
    button.disabled = true;
  }
  document.getElementById("stop_button").disabled = false;
}

function delete_item(item_name) {
  console.log(item_name);
  eel.delete_item(item_name);
  location.reload();
}

function stop_bot() {
  eel.stop_item();

  for (button of document.querySelectorAll(".user_action")) {
    button.disabled = false;
  }
  document.getElementById("stop_button").disabled = true;
}

function display_item(items) {
  for (let item of items) {
    // onclick="play_item('${item[0]}')"
    // onclick="delete_item('${item[0]}')"
  }
}
