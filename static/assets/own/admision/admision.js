var limit;

function init_busqueda() {
    limit = 8;
    init_busqueda_input();
    init_busqueda_search();
}

function init_busqueda_input() {
    document.getElementById('input_documento').oninput = function(){
        if(this.value.length === limit){
            console.log('Buscar');
        }
    };
}

function init_busqueda_search() {
    document.getElementById('select_documento').onchange = function () {
        var e = document.getElementById("select_documento");
        limit = parseInt(e.options[e.selectedIndex].getAttribute('data-length'));
        document.getElementById('input_documento').setAttribute('maxlength', limit);
    };
}