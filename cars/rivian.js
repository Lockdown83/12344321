// This code lists the last 5 presidents of Brazil and prints them to the console.

console.log("The last 5 presidents of Brazil are:");
console.log("1. Luiz Inácio Lula da Silva (2023 - present)");
console.log("2. Jair Bolsonaro (2019 - 2022)");
console.log("3. Michel Temer (2016 - 2018)");
console.log("4. Dilma Rousseff (2011 - 2016)");
console.log("5. Luiz Inácio Lula da Silva (2003 - 2010)");
for (let i = 1; i <= 5; i++) {
    console.log(`${i}. ${getPresidentName(i)}`);
}

function getPresidentName(index) {
    const presidents = [
        "Luiz Inácio Lula da Silva (2023 - present)",
        "Jair Bolsonaro (2019 - 2022)",
        "Michel Temer (2016 - 2018)",
        "Dilma Rousseff (2011 - 2016)",
        "Luiz Inácio Lula da Silva (2003 - 2010)"
    ];
    return presidents[index - 1]; // Adjust for zero-based index
}
