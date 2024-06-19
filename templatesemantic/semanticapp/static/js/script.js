// Summary Bar Graph
let ctx = document.getElementById("barChart").getContext("2d");
let chart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["2020/Q1", "2020/Q2", "2020/Q3", "2020/Q4"],
        datasets: [
            {
                label: "Gross volume ($)",
                backgroundColor: "#877f79",
                borderColor: "#417690",
                data: [26900, 28700, 27300, 29200]
            }
        ]
    },
    options: {
        title: {
            text: "Gross Volume in 2020",
            display: true
        }
    }
});

// Summary Pie Graph
let pie = document.getElementById("pieChart").getContext("2d");
let pieChart = new Chart(pie, {
    type: "line",
    data: {
        labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6'],
        datasets: [
            {
                label: "Dataset",
                data: [150, 200, 50, 310, 100, 30],
                backgroundColor: ["#c58d68"],
                borderColor: "#c58d68",
                pointStyle: 'circle',
                pointRadius: 6,
                pointHoverRadius: 15,
            }
        ]
    },
    options: {
        responsive: true,
        title: {
            text: "Gross Volume in 2020",
            display: true
        }
    }
});