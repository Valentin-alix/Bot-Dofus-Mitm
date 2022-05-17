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