function play_item(item_name)
{
    eel.play_item(item_name)
}

function display_item(items)
{
    for (const item of items)
    {
        $("table tbody").append(`<tr>
        <td>${item[0]}</td>
        <td>${item[1]}</td>
        <td><button onclick="play_item('${item[0]}')">Play</button></td>
        </tr>`); 
    }
}

