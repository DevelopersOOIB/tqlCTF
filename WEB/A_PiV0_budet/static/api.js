document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.getElementById("searchForm");
    const getAllDrinksButton = document.getElementById("getAllDrinks");
    const drinksTableBody = document.querySelector("#drinksTable tbody");

    // Function to display drinks in table
    function displayDrinks(drinks) {
        drinksTableBody.innerHTML = '';
        drinks.forEach(drink => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${drink.id}</td>
                <td>${drink.type}</td>
                <td>${drink.brand}</td>
                <td>${drink.amount}</td>
            `;
            drinksTableBody.appendChild(row);
        });
    }

    // Fetch and display all drinks
    getAllDrinksButton.addEventListener("click", async () => {
        try {
            const response = await fetch('/api/v1.0/drinks');
            if (response.ok) {
                const drinks = await response.json();
                displayDrinks(drinks);
            } else {
                console.error("Failed to fetch drinks");
            }
        } catch (error) {
            console.error("Error:", error);
        }
    });

    // Search form submission handler
    searchForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const query = document.getElementById("searchInput").value;

        try {
            const response = await fetch(`/api/v1.0/drinks/search?query=${query}`);
            if (response.ok) {
                const drinks = await response.json();
                displayDrinks(drinks);
            } else {
                console.error("Failed to fetch drinks");
            }
        } catch (error) {
            console.error("Error:", error);
        }
    });
});
