// Obtener datos incrustados desde etiquetas HTML ocultas
const clientes = JSON.parse(document.getElementById('data-clientes').textContent);
const montos = JSON.parse(document.getElementById('data-montos').textContent);

// Referencia al canvas de la gráfica
const ctx = document.getElementById('creditoChart').getContext('2d');

// Instanciar gráfico tipo doughnut
const creditoChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: clientes,
        datasets: [{
            label: 'Monto por Cliente',
            data: montos,
            backgroundColor: [
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 205, 86, 0.5)',
            ],
            borderColor: 'rgba(255, 255, 255, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: false,
        plugins: {
            legend: {
                position: 'right'
            },
            title: {
                display: true,
                text: 'Distribución de Créditos por Cliente'
            }
        }
    }
});
