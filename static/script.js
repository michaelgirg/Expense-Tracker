document.getElementById("expense-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const title = document.getElementById("title").value;
    const amount = document.getElementById("amount").value;
    const category = document.getElementById("category").value;

    await fetch("/add", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title, amount, category})
    });

    loadExpenses();
});

async function loadExpenses() {
    const res = await fetch("/expenses");
    const expenses = await res.json();
    const list = document.getElementById("expense-list");
    list.innerHTML = '';
    expenses.forEach(([id, title, amount, category]) => {
        const li = document.createElement("li");
        li.textContent = `${title} - $${amount} (${category})`;
        list.appendChild(li);
    });
}

window.onload = loadExpenses;
