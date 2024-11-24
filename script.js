function spin() {
  const reels = ['🍒', '🍋', '🍉', '⭐', '🍇'];
  const chances = [40, 30, 20, 5, 5]; // Peluang masing-masing simbol

  const getSymbol = () => {
    const random = Math.random() * 100;
    let cumulative = 0;
    for (let i = 0; i < chances.length; i++) {
      cumulative += chances[i];
      if (random <= cumulative) return reels[i];
    }
  };

  const result1 = getSymbol();
  const result2 = getSymbol();
  const result3 = getSymbol();

  document.getElementById('reel1').textContent = result1;
  document.getElementById('reel2').textContent = result2;
  document.getElementById('reel3').textContent = result3;

  const resultText = result1 === result2 && result2 === result3 ? 'Menang!' : 'Kalah!';
  document.getElementById('result').textContent = resultText;
}
