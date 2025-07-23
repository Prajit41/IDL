const quizzes = [
  { title: "Environmental Ethics", age: "13-15", type: "Value" },
  { title: "AI Boon or Boom", age: "13-15", type: "Value" },
  { title: "AI & Employment", age: "16-18", type: "Policy" },
  { title: "Space Exploration", age: "13-15", type: "Fact" },
  { title: "The Future of Space Travel", age: "19+", type: "Speculative" },
  { title: "Youth Politics", age: "19+", type: "Politics" },
  { title: "Climate Change Solutions", age: "16-18", type: "Policy" },
];

const quizGrid = document.getElementById("quizGrid");
const ageFilter = document.getElementById("ageFilter");

function renderQuizzes(filterAge) {
  quizGrid.innerHTML = "";

  const filtered = quizzes.filter((quiz) => {
    return filterAge === "all" || quiz.age === filterAge;
  });

  filtered.forEach((quiz) => {
    const card = document.createElement("div");
    card.className = "quiz-card";
    card.innerHTML = `
      <h3>${quiz.title}</h3>
      <p>Age: ${quiz.age} • Type: ${quiz.type}</p>
    `;
    quizGrid.appendChild(card);
  });
}

ageFilter.addEventListener("change", (e) => {
  renderQuizzes(e.target.value);
});

renderQuizzes("all");
