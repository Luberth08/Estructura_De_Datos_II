function simularTurnoIA() {
    fetch('/turno_ia', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        // Actualizar dados
        document.querySelectorAll('.dado').forEach((dado, index) => {
            dado.textContent = data.nuevos_dados[index];
        });
        
        // Mostrar resultados
        document.getElementById('jugada-ia').textContent = 
            `IA apostó a: ${data.jugada}`;
        document.getElementById('lanzada-ia').textContent = 
            `Lanzamiento: ${data.lanzada.join(', ')}`;
    });
}