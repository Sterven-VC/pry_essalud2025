// Función para buscar en la tabla
document.getElementById('buscar').addEventListener('keyup', function() {
  const searchText = this.value.toLowerCase().trim();
  const table = document.getElementById('example');
  const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

  Array.from(rows).forEach(row => {
      const cells = row.getElementsByTagName('td');
      const isRowVisible = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(searchText));
      row.style.display = isRowVisible ? '' : 'none';
  });
});

let rowsPerPage = 5;
let currentPage = 1;
const table = document.getElementById('example');
const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
const totalRows = rows.length;
let totalPages = Math.ceil(totalRows / rowsPerPage) || 1;

// Función para mostrar la página actual de la tabla
function displayTable() {
  for (let i = 0; i < rows.length; i++) {
      const rowIndex = i + 1;
      const isRowVisible = rowIndex > (currentPage - 1) * rowsPerPage && rowIndex <= currentPage * rowsPerPage;
      rows[i].style.display = isRowVisible ? '' : 'none';
  }

  document.getElementById('pageNum').innerText = `${currentPage} / ${totalPages}`;
}

// Función para ir a la siguiente página
function nextPage() {
  if (currentPage < totalPages) {
      currentPage++;
      displayTable();
  }
}

// Función para ir a la página anterior
function prevPage() {
  if (currentPage > 1) {
      currentPage--;
      displayTable();
  }
}

// Cargar la primera página al cargar el HTML
document.addEventListener('DOMContentLoaded', () => {
  displayTable();
});

// Obtener los parámetros de la URL
const urlParams = new URLSearchParams(window.location.search);
const errorParam = urlParams.get('error');

// Si existe el parámetro "error", mostrar la alerta
if (errorParam === 'unauthorized') {
  alert('No tienes permiso para ver este informe.');
}

// Manejar el cambio en el número de filas por página
document.getElementById('rowsPerPage').addEventListener('change', function() {
  rowsPerPage = parseInt(this.value);
  currentPage = 1;
  totalPages = Math.ceil(totalRows / rowsPerPage) || 1;
  displayTable();
});