document.getElementById('btnAgregar').addEventListener('click', function () {
    const producto = document.getElementById('producto').value;
    const cantidad = document.getElementById('cantidad').value;
    const precio = document.getElementById('precioUnitario').value;

    fetch('/agregar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ producto, cantidad, precio })
    }).then(() => location.reload());
});

document.querySelectorAll('.btnEditar').forEach((btn, index) => {
    btn.addEventListener('click', () => {
        const fila = btn.closest('tr');
        const celdas = fila.querySelectorAll('td');
        for (let i = 0; i < 3; i++) {
            const input = document.createElement('input');
            input.value = celdas[i].innerText;
            celdas[i].innerText = '';
            celdas[i].appendChild(input);
        }
        btn.style.display = 'none';
        fila.querySelector('.btnGuardar').style.display = 'inline-block';
    });
});

document.querySelectorAll('.btnGuardar').forEach((btn) => {
    btn.addEventListener('click', () => {
        const fila = btn.closest('tr');
        const inputs = fila.querySelectorAll('input');
        const id = btn.dataset.id;

        fetch('/actualizar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                id,
                producto: inputs[0].value,
                cantidad: inputs[1].value,
                precio: inputs[2].value
            })
        }).then(() => location.reload());
    });
});