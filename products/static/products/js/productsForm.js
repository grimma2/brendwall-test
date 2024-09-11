document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('product-form');
    const productTableBody = document.getElementById('product-table-body');
    const errorBlock = document.getElementById('error-block');

    // Функция для обновления таблицы продуктов
    function updateProductTable() {
        fetch('/api/v1/products/')
            .then(response => response.json())
            .then(data => {
                productTableBody.innerHTML = data.map(product => `
                    <tr>
                        <td>${product.name}</td>
                        <td>${product.description}</td>
                        <td>${product.price}</td>
                    </tr>
                `).join('');
            })
            .catch(error => console.error('Ошибка получения продуктов:', error));
    }

    // Обработчик отправки формы
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            description: formData.get('description'),
            price: formData.get('price')
        };

        fetch('/api/v1/products/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                updateProductTable();
                form.reset();
                errorBlock.textContent = '';  // Очистка блока ошибок
            } else {
                return response.json().then(errorData => {
                    let errorKeys = Object.keys(errorData)
                    let firstKey = errorKeys[0]
                    errorBlock.textContent = `Ошибка ${response.status}: ${errorData[firstKey]}`;
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorBlock.textContent = `Ошибка: ${error.message}`;
        });
    });

    // Инициализация таблицы продуктов при загрузке страницы
    updateProductTable();
});
