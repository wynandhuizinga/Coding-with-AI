function getAssets() {
  // Clear the existing table
  const assetTable = document.getElementById('assetTable');
  while (assetTable.rows.length > 0) {
   assetTable.deleteRow(-1);
  }

  // Make API call using fetch()
  fetch('http://localhost:80/assets')
     .then(response => response.json())
     .then(data => {
         // Create table header row
         const headerRow = document.createElement('tr');
         headerRow.innerHTML = '<th>ID</th><th>Amount</th><th>Manufacturer</th><th>Name</th>';
         assetTable.appendChild(headerRow);
         // Loop through assets and create table rows
         data.forEach(asset => {
             const assetRow = document.createElement('tr');
             assetRow.innerHTML = `<td>${asset.id}</td><td>${asset.amount}</td><td>${asset.manufacturer}</td><td>${asset.name}</td>`;
             assetTable.appendChild(assetRow);
         });
     })
     .catch(error => console.log(error));
}

function showMessage() {
   fetch(`http://localhost:80/total_gwp`)
       .then(response => response.text())
       .then(data => document.getElementById('message').innerText = data)
       .catch(error => console.log(error));
}