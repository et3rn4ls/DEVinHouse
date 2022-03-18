var lista = [];
var add = document.getElementById("add");
add.addEventListener('click', addItem);

var del = document.getElementById("del");
del.addEventListener('click', delItem);

var ul = document.getElementById("lista");

function addItem() {  
    var newItem = document.getElementById("item").value;
    
    if (newItem.length !== 0) {
        if (!lista.includes(newItem)) {
            lista.push(newItem);
            addLinha(newItem);
            document.getElementById("retorno").innerHTML = `Adicionado ${newItem} à sua lista!`;
            document.getElementById("item").value = '';
            setTimeout(function() {
                document.getElementById("retorno").innerHTML = '';
            }, 1000)
        } else {
            alert(`Já existe ${newItem} na sua lista de compras!`);
        }
    } else {
        alert("Por favor, informe o nome do item!");
    }
}

function addLinha(newItem) {
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(newItem));
    ul.appendChild(li);
}

function delItem() {
    var oldItem = window.prompt("Informe o nome do item que deseja remover:");
    const index = lista.indexOf(oldItem);

    if (index > -1) {
        lista.splice(index, 1);

        var li = ul.children[index];
        ul.removeChild(li);
    
    } else {
        alert("Item não encontrado na lista de compras!");
    }
}
