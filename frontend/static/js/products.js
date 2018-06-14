! function() {
    function searchFunction() {
        let td;
        let i;
        let $input = $("#search-input");
        let filter = $input.val().toUpperCase();
        let $table = $("#store-products-table");
        let tr = $table.find("tr");

        tr.each(function(i) {
            symbolTD = tr[i].getElementsByTagName("td")[0];
            descTD = tr[i].getElementsByTagName("td")[1];

            if (symbolTD || descTD) {
                let condition1 = symbolTD.innerHTML.toUpperCase().indexOf(filter) > -1
                let condition2 = descTD.innerHTML.toUpperCase().indexOf(filter) > -1

                if (condition1 || condition2) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        })
    }
    const $contentMain = $('#store-div');
    $contentMain.on('keyup', '#search-input', void 0, searchFunction)
}();