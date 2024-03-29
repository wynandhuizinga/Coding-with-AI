function getAssets() {
   fetch("/assets")
   .then(response => response.json())
   .then(data => {
       const container = document.querySelector(".container");
       data.forEach(item => {
           const card = document.createElement("div");
           card.classList.add("card");
           const title = document.createElement("h3");
           title.textContent = item.name;
           card.appendChild(title);
           const info = document.createElement("p");
           info.textContent = `ID: ${item.id}, Manufacturer: ${item.manufacturer}, Amount: ${item.amount}`;
           card.appendChild(info);
           container.appendChild(card);
       });
       const totalCountElement = document.getElementById("total-count");
       totalCountElement.textContent = `${data.length} Total Count`;
   })
   .catch(error => console.log(error));
}

function getGWP() {
   fetch("/total_gwp")
   .then(response => response.json())
   .then(data => {
       const messageContainer = document.querySelector("#message-container");
       const message = document.createElement("p");
       message.textContent = data.message;
       messageContainer.appendChild(message);
   })
   .catch(error => console.log(error));
}

function handleResponse(data) {
   var cards = document.querySelectorAll('.card'); // clear existing cards
   for (var i = 0; i < data.length; i++) {
       var newCard = document.createElement('div');
       newCard.classList.add('card');
       var cardTitle = document.createElement('h3');
       cardTitle.textContent = data[i].name;
       newCard.appendChild(cardTitle);
       var cardInfo = document.createElement('p');
       cardInfo.textContent = "ID: " + data[i].id + ", Manufacturer: " + data[i].manufacturer + ", Amount: " + data[i].amount;
       newCard.appendChild(cardInfo);
       document.body.appendChild(newCard);
   }
   var totalCount = document.getElementById('total-count');
   totalCount.innerHTML = "Total Count: " + data.length;
}