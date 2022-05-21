function play_item(item_name)
{
    eel.play_item(item_name);
}

function stop_bot()
{
    eel.stop_item();
}

function display_item(items)
{
    for (const item of items)
    {
        $("table tbody").append(`<tr>
        <td>${item[0]}</td>
        <td><button class="btn btn-success" onclick="play_item('${item[0]}')">Play</button></td>
        </tr>`); 
    }
}

