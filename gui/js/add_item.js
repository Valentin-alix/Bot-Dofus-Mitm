// TO GET ITEM INSERTED AND EVENTUALLY ADD IT TO DATABASE
// TRY EVENT LISTENER ON HREF ADD ITEM AVEC PARAM DE ITEM POUR VOIR
eel.expose(on_inserted_item);
function on_inserted_item(item)
{   
    last_path_name = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
    if (last_path_name == "waiting_item.html" || last_path_name == "add_item.html")
    {   
        localStorage.setItem("item", JSON.stringify(item));
        redirect("add_item.html");
    }
}

function update_item()
{
    const edited_item = document.getElementById("inserted_item");
    const name_item = document.getElementById("name_item").value;
    let dict_edited_item = [];
    const lines = edited_item.childNodes;
    for (const line of lines)
    {   
        switch (line.nodeName)
        {   
            case "BR":
                continue;
            //FIX ME VERIFIER QUE TYPE DANS DB
            case "LABEL":
                {
                    dict_edited_item.push({});
                    dict_edited_item[dict_edited_item.length-1]['Type'] = line.textContent;
                    continue;
                }
            case "INPUT":
                let parsed_int = parseInt(line.value);
                switch (line.id)
                {
                    case "Value":
                        if (Number.isInteger(parsed_int))
                        {
                            dict_edited_item[dict_edited_item.length-1]['Value'] = line.value;
                            continue;
                        }
                        else
                        {
                            alert("Veuillez remplir tous les champs avec des valeurs corrects");
                            return
                        }
                    case "Line":
                        if (Number.isInteger(parsed_int) && parsed_int <= 13)
                        {
                            dict_edited_item[dict_edited_item.length-1]['Line'] = line.value;
                            continue;
                        }
                        else
                        {
                            alert("Veuillez remplir tous les champs avec des valeurs corrects");
                            return
                        }
                    case "Column":
                        if (Number.isInteger(parsed_int) && parsed_int <= 2)
                        {
                            dict_edited_item[dict_edited_item.length-1]['Column'] = line.value;
                            continue;
                        }
                        else
                        {
                            alert("Veuillez remplir tous les champs avec des valeurs corrects");
                            return
                        }
                }
        }
    }
    //ADD DICT TO DB WITH NAME ITEM
    redirect("waiting_item.html");
}