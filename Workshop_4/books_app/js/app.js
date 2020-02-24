const URL = "http://localhost:8000";
$(()=>{

    //pobranie ksiazek z mojego serwera
    let table = $("table tbody");

    $.ajax({
        url: `${URL}/book`,
        type: "GET",

    }).done((response) => {
        console.log(response);
        response.forEach((item, idx) => {
            let tr = $(`<tr>
                    <td>${idx + 1}</td>
                    <td>${item.author}</td>
                    <td>${item.title}</td>
                    <td>${item.isbn}</td>
                    </tr>`);
            table.append(tr)

        })
    })
});