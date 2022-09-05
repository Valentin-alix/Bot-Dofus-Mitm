const VAR_REGEX = /[^A-Za-z0-9]+/;

eel.expose(on_inserted_item);
function on_inserted_item(item) {
  last_path_name = window.location.href.substring(
    window.location.href.lastIndexOf("/") + 1
  );
  if (
    last_path_name == "waiting_item.html" ||
    last_path_name == "add_item.html"
  ) {
    localStorage.setItem("item", JSON.stringify(item));
    redirect("add_item.html");
  }
}

function update_item() {
  let name_item = document.getElementById("name_item").value;

  if (VAR_REGEX.test(name_item)) {
    alert(
      "Veuillez mettre un nom d'item valide (seulement des chiffres et des lettres)"
    );
    return;
  }

  let dict_edited_item = [];

  let all_types = document.querySelectorAll("#Type");
  let all_values = document.querySelectorAll("#Value");
  let all_columns = document.querySelectorAll("#Column");
  let all_lines = document.querySelectorAll("#Line");
  for (var i = 0; i < all_types.length; i++) {
    if (
      !Number.isInteger(parseInt(all_lines[i].value)) ||
      !Number.isInteger(parseInt(all_columns[i].value)) ||
      !Number.isInteger(parseInt(all_values[i].value))
    ) {
      alert("Veuillez compléter les champs avec des valeurs valides");
      return;
    }
    dict_edited_item.push({});
    dict_edited_item[dict_edited_item.length - 1]["Type"] =
      all_types[i].textContent;
    dict_edited_item[dict_edited_item.length - 1]["Value"] =
      all_values[i].value;
    dict_edited_item[dict_edited_item.length - 1]["Line"] = all_lines[i].value;
    dict_edited_item[dict_edited_item.length - 1]["Column"] =
      all_columns[i].value;
  }
  eel.insert_item(dict_edited_item, name_item);
  redirect("waiting_item.html");
}
